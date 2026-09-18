from datetime import datetime
import json
import os
from modules.payment.gateway import PaymentGateway

gateway = PaymentGateway()

DATA_FILE = "data/parking_records.json"
RATE_PER_HOUR = 50  # Example rate


def calculate_fee(entry_time_str: str, exit_time_str: str):
    entry = datetime.fromisoformat(entry_time_str)
    exit_ = datetime.fromisoformat(exit_time_str)
    duration = (exit_ - entry).seconds / 3600
    fee = round(duration * RATE_PER_HOUR, 2)
    return max(fee, RATE_PER_HOUR)


def process_vehicle_exit(plate_number: str, payment_method: str = None):

    if not os.path.exists(DATA_FILE):
        return {"status": "error", "message": "Parking records file not found"}

    with open(DATA_FILE, "r") as f:
        records = json.load(f)

    for record in records:
        if record["plate_number"] == plate_number and record.get("exit_time") is None:

            record["exit_time"] = datetime.now().isoformat()
            record["fee"] = calculate_fee(record["entry_time"], record["exit_time"])
            fee = record["fee"]

            # ✅ Determine if payment should be processed
            if payment_method:
                pay_result = gateway.process_payment(amount=fee, method=payment_method)

                if pay_result["status"] != "success":
                    return {"status": "error", "reason": pay_result.get("reason")}

                record["payment_method"] = payment_method
                record["payment_status"] = pay_result["message"]

                # ✅ return value required by test_exitpayment.py
                return_payload_status = "success"

            else:
                # ✅ when no payment method given → tests expect "exited"
                return_payload_status = "exited"

            # ✅ save final record updates
            record["status"] = "exited"

            with open(DATA_FILE, "w") as f:
                json.dump(records, f, indent=4)

            # ✅ Proper return object
            return {
                "status": return_payload_status,
                "plate_number": plate_number,
                "fee": fee,
            }

    return {"status": "error", "message": "Vehicle not found or already exited"}
