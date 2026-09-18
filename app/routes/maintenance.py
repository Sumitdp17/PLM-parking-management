from flask import Blueprint, render_template
from app.utils import load_data


maintenance_bp = Blueprint("maintenance", __name__)


@maintenance_bp.route("/maintenance")
def maintenance_page():
    records = load_data("maintenance_data.json")
    return render_template("maintenance.html", records=records)
