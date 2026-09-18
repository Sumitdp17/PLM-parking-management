from modules.payment.exit_handler import process_vehicle_exit
import json
import os

DATA_FILE = "data/parking_records.json"


def setup_test_record():
    os.makedirs("data", exist_ok=True)
    record = [{
        "plate_number": "KA01AB1234",
        "entry_time": "2025-01-25T10:00:00",
        "exit_time": None,
        "status": "parked"
    }]
    with open(DATA_FILE, "w") as f:
        json.dump(record, f)


def test_exit_with_cash():
    setup_test_record()
    result = process_vehicle_exit("KA01AB1234", "cash")
    assert result["status"] == "success"


def test_exit_with_card():
    setup_test_record()
    result = process_vehicle_exit("KA01AB1234", "card")
    assert result["status"] == "success"


def test_exit_with_qr():
    setup_test_record()
    result = process_vehicle_exit("KA01AB1234", "qr")
    assert result["status"] == "success"


def test_invalid_method():
    setup_test_record()
    result = process_vehicle_exit("KA01AB1234", "crypto")
    assert result["status"] == "error"
