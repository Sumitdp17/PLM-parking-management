# app/routes/validate.py
from flask import Blueprint, request, render_template

validate_bp = Blueprint("validate", __name__)


@validate_bp.route("/validate", methods=["GET", "POST"])
def validate_receipt():
    if request.method == "POST":
        data = request.form["qr_text"]
        try:
            plate, hours, amount = data.split("|")
            return render_template("validate_success.html",
                                   plate=plate, hours=hours, amount=amount)
        except Exception:  # <-- replaced bare except
            return render_template("validate_fail.html")

    return render_template("validate.html")
