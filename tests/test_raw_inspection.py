import zipfile

import pytest

from telecom_pulse.raw_inspection import RawInspectionError, inspect_raw_zip


def test_inspect_raw_zip_profiles_csv(tmp_path):
    zip_path = tmp_path / "sample.zip"
    with zipfile.ZipFile(zip_path, "w") as archive:
        archive.writestr(
            "sample.csv",
            "UF;Grupo;Acessos\nSP;EXEMPLO;10\nRJ;EXEMPLO;5\n",
        )

    profile = inspect_raw_zip(zip_path)

    assert profile.members == ("sample.csv",)
    assert len(profile.csv_members) == 1
    csv_profile = profile.csv_members[0]
    assert csv_profile.delimiter == ";"
    assert csv_profile.headers == ("UF", "Grupo", "Acessos")
    assert csv_profile.sample_rows == 2


def test_inspect_raw_zip_rejects_invalid_zip(tmp_path):
    path = tmp_path / "not.zip"
    path.write_text("not a zip", encoding="utf-8")

    with pytest.raises(RawInspectionError, match="valid ZIP"):
        inspect_raw_zip(path)


def test_inspect_raw_zip_requires_csv(tmp_path):
    zip_path = tmp_path / "sample.zip"
    with zipfile.ZipFile(zip_path, "w") as archive:
        archive.writestr("readme.txt", "hello")

    with pytest.raises(RawInspectionError, match="no CSV"):
        inspect_raw_zip(zip_path)
