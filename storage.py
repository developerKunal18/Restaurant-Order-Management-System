import json
import os


def load_data(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Expected a JSON list.")

        return data

    except (json.JSONDecodeError, OSError, ValueError) as error:
        raise RuntimeError(
            f"Could not read {filename}: {error}"
        ) from error


def save_data(filename, data):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    temporary_file = filename + ".tmp"

    with open(temporary_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    os.replace(temporary_file, filename)
