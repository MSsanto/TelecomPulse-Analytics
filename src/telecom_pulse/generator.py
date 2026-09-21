REFERENCE_ROWS = [
    {
        "incident_id": "INC-0001",
        "site_id": "SITE-001",
        "carrier": " carrier a ",
        "opened_at": "2026-09-01T10:00:00Z",
        "restored_at": "2026-09-01T11:00:00Z",
        "status": "RESOLVED",
        "cause_category": " Fiber Break ",
        "region": "SE",
        "link_type": "Fiber",
        "source": "synthetic",
    },
    {
        "incident_id": "INC-0002",
        "site_id": "SITE-002",
        "carrier": "Carrier B",
        "opened_at": "2026-09-02T12:00:00Z",
        "restored_at": "2026-09-02T12:30:00Z",
        "status": "resolved",
        "cause_category": "Power",
        "region": "SE",
        "link_type": "fiber",
        "source": "synthetic",
    },
    {
        "incident_id": "INC-0003",
        "site_id": "SITE-001",
        "carrier": "Carrier A",
        "opened_at": "2026-09-03T14:00:00Z",
        "restored_at": "2026-09-03T15:30:00Z",
        "status": "resolved",
        "cause_category": "Carrier Outage",
        "region": "SE",
        "link_type": "fiber",
        "source": "synthetic",
    },
    {
        "incident_id": "INC-0004",
        "site_id": "SITE-003",
        "carrier": "Carrier C",
        "opened_at": "2026-09-04T08:00:00Z",
        "restored_at": "",
        "status": "open",
        "cause_category": "Unknown",
        "region": "S",
        "link_type": "radio",
        "source": "synthetic",
    },
]

FIELDS = tuple(REFERENCE_ROWS[0])


def generate_reference_dataset(path) -> None:
    """Write the public synthetic reference dataset used by tests and demos."""
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = [",".join(FIELDS)]
    rows.extend(",".join(str(row[field]) for field in FIELDS) for row in REFERENCE_ROWS)
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
