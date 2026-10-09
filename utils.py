import uuid
from datetime import datetime


def generate_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"


def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def find_by_id(records, record_id, key="id"):
    return next(
        (
            record for record in records
            if record.get(key) == record_id
        ),
        None
    )


def read_positive_number(prompt):
    try:
        number = float(input(prompt))

        if number <= 0:
            print("Enter a number greater than zero.")
            return None

        return round(number, 2)

    except ValueError:
        print("Invalid number.")
        return None


def money(amount):
    return f"₹{amount:.2f}"
