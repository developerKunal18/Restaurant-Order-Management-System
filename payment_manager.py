from config import ORDER_FILE, PAYMENT_FILE, PAYMENT_METHODS
from storage import load_data, save_data
from utils import generate_id, current_datetime, find_by_id, money


def record_payment():
    orders = load_data(ORDER_FILE)
    payments = load_data(PAYMENT_FILE)

    order_id = input("Order ID: ").strip()
    order = find_by_id(orders, order_id)

    if not order:
        print("Order not found.")
        return

    if order["status"] == "Cancelled":
        print("Cannot pay for a cancelled order.")
        return

    if order["payment_status"] == "Paid":
        print("This order is already paid.")
        return

    print("Amount Due:", money(order["total"]))

    print("\nPayment Methods:")

    for index, method in enumerate(PAYMENT_METHODS, 1):
        print(f"{index}. {method}")

    try:
        choice = int(input("Select method: "))

        if not 1 <= choice <= len(PAYMENT_METHODS):
            print("Invalid choice.")
            return

    except ValueError:
        print("Invalid choice.")
        return

    payment = {
        "id": generate_id("PAY"),
        "order_id": order_id,
        "amount": order["total"],
        "method": PAYMENT_METHODS[choice - 1],
        "date": current_datetime()
    }

    payments.append(payment)
    order["payment_status"] = "Paid"

    save_data(PAYMENT_FILE, payments)
    save_data(ORDER_FILE, orders)

    print("\nPayment recorded successfully.")
    print("Receipt ID:", payment["id"])
    print("Amount:", money(payment["amount"]))
    print("Method:", payment["method"])


def view_payments():
    payments = load_data(PAYMENT_FILE)

    if not payments:
        print("No payments recorded.")
        return

    for payment in payments:
        print("-" * 40)
        print("Receipt:", payment["id"])
        print("Order:", payment["order_id"])
        print("Amount:", money(payment["amount"]))
        print("Method:", payment["method"])
        print("Date:", payment["date"])
