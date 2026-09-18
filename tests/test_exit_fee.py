import os
import json
from datetime import datetime, timedelta
from modules.payment.exit_handler import calculate_fee, process_vehicle_exit


def test_calculate_fee_one_hour():
    entry = datetime.now() - timedelta(hours=1)
    exit_ = datetime.now()
    fee = calculate_fee(entry.isoformat(), exit_.isoformat())
    assert fee >= 50


def test_process_vehicle_exit(tmp_path):
    os.chdir(tmp_path)
    os.makedirs("data", exist_ok=True)
    entry_time = datetime.now().isoformat()
    data = [{"plate_number": "KA03ZZ0001", "entry_time": entry_time, "exit_time": None}]
    with open("data/parking_records.json", "w") as f:
        json.dump(data, f)

    record = process_vehicle_exit("KA03ZZ0001")
    assert record["status"] == "exited"
    assert "fee" in record
