
import json

def save_as_json(data, filename):
    """Saves the given data to a JSON file."""
    try:    
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
            #Uses indent=4 for readability
            print(f"Data saved to {filename}")
            print("\n")
    except Exception as e:
            print(f"Failed to save data to {filename}: {e}")
