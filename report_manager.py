from datetime import datetime
from config import MENU_FILE, ORDER_FILE, PAYMENT_FILE
from storage import load_data
from utils import money


def sales_report():
    orders = load_data(ORDER_FILE)
    payments = load_data(PAYMENT_FILE)

    today = datetime.now().strftime("%Y-%m-%d")

    todays_orders = [
        order for order in orders
        if order["created_at"].startswith(today)
        and order["status"] != "Cancelled"
    ]

    todays_payments = [
        payment for payment in payments
        if payment["date"].startswith(today)
    ]

    print("\n========== TODAY'S SALES ==========")
    print("Date:", today)
    print("Orders:", len(todays_orders))
    print(
        "Order Value:",
        money(sum(order["total"] for order in todays_orders))
    )
    print(
        "Payments Received:",
        money(sum(payment["amount"] for payment in todays_payments))
    )


def popular_items_report():
    orders = load_data(ORDER_FILE)

    quantities = {}

    for order in orders:
        if order["status"] == "Cancelled":
            continue

        for item in order["items"]:
            name = item["name"]
            quantities[name] = (
                quantities.get(name, 0) + item["quantity"]
            )

    if not quantities:
        print("No order items found.")
        return

    print("\n========== POPULAR ITEMS ==========")

    for name, quantity in sorted(
        quantities.items(),
        key=lambda entry: (-entry[1], entry[0])
    ):
        print(f"{name}: {quantity} sold")


def pending_payment_report():
    orders = load_data(ORDER_FILE)

    pending = [
        order for order in orders
        if order["payment_status"] != "Paid"
        and order["status"] != "Cancelled"
    ]

    print("\n========== PENDING PAYMENTS ==========")

    if not pending:
        print("No pending payments.")
        return

    for order in pending:
        print(
            order["id"],
            order["customer_name"],
            money(order["total"])
        )
