# app/routes/exit.py
from datetime import datetime
from flask import Blueprint, request, render_template, send_file
import os

from modules.payment.calculator import calculate_fee
from modules.payment.receipt import generate_receipt
from app.utils import load_data, save_data


exit_bp = Blueprint("exit", __name__)


@exit_bp.route("/", methods=["GET", "POST"])
def vehicle_exit():
    data = load_data("parking_data.json")
    vehicles = data.get("vehicles", [])

    if request.method == "POST":
        plate = request.form["plate"]

        record = next(
            (v for v in vehicles if v.get("plate") == plate and v.get("exit_time") is None),
            None,
        )

        if record is None:
            return "❌ Vehicle not currently parked or not found", 400

        exit_time = datetime.now().isoformat()
        fee, hours = calculate_fee(record["entry_time"], exit_time)

        record["exit_time"] = exit_time
        record["amount"] = fee
        save_data("parking_data.json", data)

        os.makedirs("receipts", exist_ok=True)
        receipt_path = f"receipts/{plate}.pdf"
        generate_receipt(receipt_path, plate, hours, fee)

        return send_file(receipt_path, as_attachment=True)

    return render_template("exit.html")
