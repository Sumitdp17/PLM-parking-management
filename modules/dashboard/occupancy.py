
from app.utils import load_data

TOTAL_SLOTS = 20


def get_occupancy():
    data = load_data("parking_data.json")
    vehicles = data.get("vehicles", [])

    occupied = sum(1 for v in vehicles if v.get("exit_time") is None)
    free = TOTAL_SLOTS - occupied
    return occupied, free
