import os
import json
from modules.parking.walkin_handler import detect_unknown_vehicle, register_walkin_vehicle, DEFAULT_CUSTOMER_ID


def test_detect_unknown_vehicle():
    assert detect_unknown_vehicle("KA03ZZ0001") is True
    assert detect_unknown_vehicle("KA01AB1234") is False


def test_register_walkin_vehicle(tmp_path):
    os.chdir(tmp_path)
    result = register_walkin_vehicle("KA09AA9999")
    assert result["customer_id"] == DEFAULT_CUSTOMER_ID
    assert os.path.exists("data/parking_records.json")
    with open("data/parking_records.json") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["plate_number"] == "KA09AA9999"
