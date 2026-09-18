import json
import os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')


def get_default_parking_data():
    """Returns the default, empty state for parking_data.json."""
    # Define a default set of parking slots
    default_slots = {}

    for i in range(1, 21):  # Create 20 slots (S1 to S20)
        default_slots[f'S{i}'] = {'status': 'available', 'vehicle_plate': None}

    return {
        'vehicles': [],  # This will store active vehicle logs
        'barriers': {
            'entry': {'status': 'closed'},
            'exit': {'status': 'closed'}
        },
        'slots': default_slots  # Add the new slots dictionary
    }


def load_data(filename):
    """Loads data from a JSON file, ensuring default structure."""
    filepath = os.path.join(DATA_FILE_PATH, filename)

    if filename == 'parking_data.json':
        default_data = get_default_parking_data()
    else:
        default_data = {}

    if not os.path.exists(filepath):
        return default_data  # File doesn't exist, return default

    try:
        with open(filepath, 'r') as f:
            content = f.read()
            if not content:
                return default_data  # Handle empty file

            data = json.loads(content)

            if filename == 'parking_data.json':
                # Ensure top-level keys exist
                for key, value in default_data.items():
                    data.setdefault(key, value)

                # --- THIS IS THE NEW FIX ---
                # If the 'slots' key exists but is empty (from an old file),
                # populate it with the default slots.
                if not data['slots']:
                    data['slots'] = default_data['slots']
                # --- END NEW FIX ---

            return data

    except (json.JSONDecodeError, KeyError):
        # File is corrupt or bad structure, return default
        return default_data


def save_data(filename, data):
    """Saves data to a JSON file in the data/ directory."""
    filepath = os.path.join(DATA_FILE_PATH, filename)

    # Ensure the data directory exists
    os.makedirs(DATA_FILE_PATH, exist_ok=True)

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
