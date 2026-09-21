from __future__ import annotations

from collections.abc import Iterable

import pandas as pd


def merge_intervals(
    intervals: Iterable[tuple[pd.Timestamp, pd.Timestamp]],
) -> list[tuple[pd.Timestamp, pd.Timestamp]]:
    """Merge overlapping or touching intervals."""
    ordered = sorted(intervals, key=lambda item: item[0])
    if not ordered:
        return []

    merged = [ordered[0]]
    for start, end in ordered[1:]:
        prev_start, prev_end = merged[-1]
        if start <= prev_end:
            merged[-1] = (prev_start, max(prev_end, end))
        else:
            merged.append((start, end))
    return merged


def _clipped_intervals(
    frame: pd.DataFrame,
    window_start: pd.Timestamp,
    window_end: pd.Timestamp,
) -> list[tuple[pd.Timestamp, pd.Timestamp]]:
    resolved = frame[
        frame["status"].eq("resolved")
        & frame["opened_at"].notna()
        & frame["restored_at"].notna()
    ]
    intervals: list[tuple[pd.Timestamp, pd.Timestamp]] = []
    for row in resolved.itertuples():
        start = max(row.opened_at, window_start)
        end = min(row.restored_at, window_end)
        if start < end:
            intervals.append((start, end))
    return intervals


def downtime_minutes_without_overlap(frame: pd.DataFrame) -> float:
    """Calculate resolved downtime without double-counting overlapping incidents."""
    resolved = frame[
        frame["status"].eq("resolved")
        & frame["opened_at"].notna()
        & frame["restored_at"].notna()
    ]
    intervals = [(row.opened_at, row.restored_at) for row in resolved.itertuples()]
    return round(
        sum((end - start).total_seconds() / 60 for start, end in merge_intervals(intervals)),
        2,
    )


def effective_downtime_minutes(
    frame: pd.DataFrame,
    window_start: pd.Timestamp,
    window_end: pd.Timestamp,
) -> float:
    """Calculate overlap-safe downtime across sites inside a fixed window."""
    total = 0.0
    for _, site_frame in frame.groupby("site_id", dropna=False):
        intervals = _clipped_intervals(site_frame, window_start, window_end)
        total += sum(
            (end - start).total_seconds() / 60
            for start, end in merge_intervals(intervals)
        )
    return round(total, 2)


def availability_pct(
    frame: pd.DataFrame,
    window_start: pd.Timestamp,
    window_end: pd.Timestamp,
) -> float:
    """Return site-time availability percentage for a fixed analysis window."""
    total_minutes = (window_end - window_start).total_seconds() / 60
    if total_minutes <= 0:
        raise ValueError("Analysis window must be positive")

    site_count = int(frame["site_id"].nunique())
    if site_count == 0:
        return 100.0

    denominator = site_count * total_minutes
    downtime = effective_downtime_minutes(frame, window_start, window_end)
    value = max(0.0, 1 - downtime / denominator) * 100
    return round(value, 4)


def recurrence_count(frame: pd.DataFrame) -> int:
    """Count incidents beyond the first occurrence per site."""
    counts = frame.groupby("site_id").size()
    return int((counts - 1).clip(lower=0).sum())
