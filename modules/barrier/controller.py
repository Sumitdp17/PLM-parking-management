import time
from app.utils import load_data, save_data


def open_entry_barrier():
    """Simulates opening the entry barrier."""

    # Load current state
    state = load_data('parking_data.json')

    # Update the barrier state
    state['barriers']['entry'] = {
        'status': 'open',
        'last_opened': time.time()
    }

    # Save the new state
    save_data('parking_data.json', state)

    print("SIMULATION: Entry barrier opened.")

    # Simulate barrier closing after 5 seconds
    # In a real app, this would be a separate thread or sensor trigger
    # state['barriers']['entry']['status'] = 'closed'
    # save_data('parking_data.json', state)
    # print("SIMULATION: Entry barrier auto-closed.")

    return True
