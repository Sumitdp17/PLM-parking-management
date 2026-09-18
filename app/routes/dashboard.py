# app/routes/dashboard.py
from flask import Blueprint, render_template, jsonify
from modules.dashboard.occupancy import get_occupancy

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def dashboard_view():
    occupied, free = get_occupancy()
    return render_template("dashboard.html", occupied=occupied, free=free)


@dashboard_bp.route("/data")
def dashboard_data():
    occupied, free = get_occupancy()
    return jsonify({"occupied": occupied, "free": free})
