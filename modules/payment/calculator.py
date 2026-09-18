
from datetime import datetime


def calculate_fee(entry_time, exit_time):
    entry = datetime.fromisoformat(entry_time)
    exit = datetime.fromisoformat(exit_time)

    hours = max(1, round((exit - entry).total_seconds() / 3600))
    fee = hours * 20
    return fee, hours
