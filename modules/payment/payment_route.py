from flask import Blueprint, request, jsonify, render_template
from modules.payment.gateway import (
    process_card_payment,
    process_cash_payment,
    process_qr_payment
)


payment_bp = Blueprint("payment", __name__)


@payment_bp.route("/pay", methods=["GET"])
def payment_page():
    return render_template("payment.html")


@payment_bp.route("/process-payment", methods=["POST"])
def process_payment():
    data = request.json
    amount = data.get("amount")
    method = data.get("method")

    if method == "card":
        card_number = data.get("card_number")
        return jsonify(process_card_payment(card_number, amount))

    if method == "cash":
        return jsonify(process_cash_payment(amount))

    if method == "qr":
        qr = data.get("qr_code")
        return jsonify(process_qr_payment(qr, amount))

    return jsonify({"status": "failed", "reason": "Unknown method"})
