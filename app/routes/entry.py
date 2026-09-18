from flask import Blueprint, jsonify, render_template, request
from modules.barrier.controller import open_entry_barrier
from modules.parking.manager import log_vehicle_entry
# Import the new parking manager for PLM-5

entry_bp = Blueprint("entry", __name__)


@entry_bp.route("/", methods=["GET"])
def entry_page():
    """Serves the main vehicle entry page."""
    # This renders the HTML file from app/templates/entry.html
    return render_template("entry.html", title="Entry Kiosk")


@entry_bp.route("/simulate_entry", methods=["POST"])
def simulate_entry():
    """
    Handles the simulated vehicle entry.
    This fulfills PLM-4 (Open Barrier) and PLM-5 (Log Entry)
    """

    data = request.get_json()
    plate = data.get('plate')

    if not plate:
        return jsonify({"status": "error", "message": "No plate provided."}), 400

    try:
        # --- This is PLM-4 ---
        open_entry_barrier()

        # --- THIS IS THE NEW CODE FOR PLM-5 ---
        new_vehicle = log_vehicle_entry(plate)
        # --- END OF NEW CODE ---

        # Send updated success response to the UI
        return jsonify({
            "status": "success",
            "message": f"Barrier Opened for {plate}. Please proceed to Slot {new_vehicle['slot']}",
            "plate": plate,
            "slot": new_vehicle['slot']
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
