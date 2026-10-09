from config import CUSTOMER_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_customer():
    customers = load_data(CUSTOMER_FILE)

    name = input("Customer Name: ").strip()
    phone = input("Phone Number: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    if not phone.isdigit() or not 10 <= len(phone) <= 15:
        print("Enter a valid phone number containing 10–15 digits.")
        return

    customer = {
        "id": generate_id("CUS"),
        "name": name,
        "phone": phone
    }

    customers.append(customer)
    save_data(CUSTOMER_FILE, customers)

    print("Customer registered:", customer["id"])


def view_customers():
    customers = load_data(CUSTOMER_FILE)

    if not customers:
        print("No customers found.")
        return

    for customer in customers:
        print(
            customer["id"],
            customer["name"],
            customer["phone"]
        )


def search_customer():
    customers = load_data(CUSTOMER_FILE)
    customer_id = input("Customer ID: ").strip()

    customer = find_by_id(customers, customer_id)

    if customer:
        print(customer)
    else:
        print("Customer not found.")
