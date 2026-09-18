
from flask import Blueprint, request, jsonify
from modules.payment.gateway import (
    process_card_payment,
    process_cash_payment,
    process_qr_payment
)

payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/pay", methods=["POST"])
def process_payment():
    data = request.json
    method = data.get("method")
    amount = data.get("amount")
    qr_code = data.get("qr_code")

    if method == "card":
        return jsonify(process_card_payment(amount))

    elif method == "cash":
        return jsonify(process_cash_payment(amount))

    elif method == "qr":
        return jsonify(process_qr_payment(amount, qr_code))

    return jsonify({"error": "Invalid payment method"}), 400
