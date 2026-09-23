from __future__ import annotations

import csv
import io
import json
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path


class RawInspectionError(RuntimeError):
    pass


@dataclass(frozen=True)
class CsvMemberProfile:
    member: str
    byte_size: int
    encoding: str
    delimiter: str
    headers: tuple[str, ...]
    sample_rows: int


@dataclass(frozen=True)
class ZipProfile:
    zip_path: str
    members: tuple[str, ...]
    csv_members: tuple[CsvMemberProfile, ...]


def _decode_csv(payload: bytes) -> tuple[str, str]:
    for encoding in ("utf-8-sig", "utf-8", "latin-1"):
        try:
            return payload.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    raise RawInspectionError("CSV member encoding could not be identified")


def inspect_raw_zip(zip_path: Path) -> ZipProfile:
    if not zip_path.is_file():
        raise RawInspectionError(f"raw ZIP not found: {zip_path}")

    try:
        archive = zipfile.ZipFile(zip_path)
    except zipfile.BadZipFile as exc:
        raise RawInspectionError("raw artifact is not a valid ZIP") from exc

    with archive:
        members = tuple(name for name in archive.namelist() if not name.endswith("/"))
        csv_names = tuple(name for name in members if name.lower().endswith(".csv"))
        if not csv_names:
            raise RawInspectionError("raw ZIP contains no CSV members")

        profiles: list[CsvMemberProfile] = []
        for member in csv_names:
            payload = archive.read(member)
            text, encoding = _decode_csv(payload[:262144])
            lines = text.splitlines()
            if not lines:
                raise RawInspectionError(f"empty CSV member: {member}")

            sample = "\n".join(lines[:50])
            try:
                dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
                delimiter = dialect.delimiter
            except csv.Error:
                delimiter = ";"

            reader = csv.reader(io.StringIO(text), delimiter=delimiter)
            try:
                headers = tuple(next(reader))
            except StopIteration as exc:
                raise RawInspectionError(f"missing header row: {member}") from exc

            profiles.append(
                CsvMemberProfile(
                    member=member,
                    byte_size=archive.getinfo(member).file_size,
                    encoding=encoding,
                    delimiter=delimiter,
                    headers=headers,
                    sample_rows=max(0, min(len(lines) - 1, 49)),
                )
            )

    return ZipProfile(
        zip_path=str(zip_path),
        members=members,
        csv_members=tuple(profiles),
    )


def write_profile(profile: ZipProfile, output_path: Path) -> None:
    payload = asdict(profile)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
