import json
import os
from datetime import datetime

DEFAULT_CUSTOMER_ID = 9999
DATA_FILE = "data/parking_records.json"


def detect_unknown_vehicle(plate_number: str) -> bool:
    """Detect if a vehicle is 'walk-in' (not in system)."""
    known_plates = load_known_plates()
    return plate_number not in known_plates


def load_known_plates():
    """Simulate a known plates list (in real system, from DB)."""
    return ["KA01AB1234", "KA02XY9876"]


def register_walkin_vehicle(plate_number: str):
    """Register an unknown (walk-in) vehicle under default customer."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    record = {
        "plate_number": plate_number,
        "customer_id": DEFAULT_CUSTOMER_ID,
        "status": "walk-in",
        "entry_time": datetime.now().isoformat()
    }

    # Write to local JSON for simulation
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(record)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return record
