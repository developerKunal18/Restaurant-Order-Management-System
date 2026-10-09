import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

MENU_FILE = os.path.join(DATA_DIR, "menu.json")
CUSTOMER_FILE = os.path.join(DATA_DIR, "customers.json")
ORDER_FILE = os.path.join(DATA_DIR, "orders.json")
PAYMENT_FILE = os.path.join(DATA_DIR, "payments.json")

GST_RATE = 5

ORDER_STATUSES = [
    "Placed",
    "Preparing",
    "Ready",
    "Served",
    "Cancelled"
]

PAYMENT_METHODS = [
    "Cash",
    "UPI",
    "Card"
]

CATEGORIES = [
    "Starters",
    "Main Course",
    "Snacks",
    "Beverages",
    "Desserts"
]
