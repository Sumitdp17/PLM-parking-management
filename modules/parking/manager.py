import time
from app.utils import load_data, save_data


def find_available_slot(slots_data):
    """Finds the first available parking slot."""
    for slot_id, details in slots_data.items():
        if details['status'] == 'available':
            return slot_id
    return None  # No available slots


def log_vehicle_entry(plate_number):
    """
    Logs a new vehicle entry, assigns a slot, and saves it.
    This fulfills PLM-5.
    """
    data = load_data('parking_data.json')

    # 1. Find an available slot
    assigned_slot = find_available_slot(data['slots'])

    if not assigned_slot:
        print("ERROR: No available parking slots.")
        raise Exception("No available parking slots.")

    entry_time = time.time()

    # 2. Create new vehicle record
    new_vehicle_record = {
        'plate': plate_number,
        'entry_time': entry_time,
        'slot': assigned_slot,
        'status': 'parked'
    }

    # 3. Add vehicle to the main list
    data['vehicles'].append(new_vehicle_record)

    # 4. Update the slot status
    data['slots'][assigned_slot] = {
        'status': 'occupied',
        'vehicle_plate': plate_number,
        'entry_time': entry_time
    }

    # 5. Save the updated data
    save_data('parking_data.json', data)

    print(f"LOG: Vehicle {plate_number} entered, assigned to {assigned_slot}.")

    return new_vehicle_record
