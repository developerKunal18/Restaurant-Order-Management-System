from config import MENU_FILE, CATEGORIES
from storage import load_data, save_data
from utils import generate_id, find_by_id, read_positive_number, money


def add_menu_item():
    menu = load_data(MENU_FILE)

    name = input("Food Name: ").strip()

    if not name:
        print("Food name is required.")
        return

    if any(item["name"].casefold() == name.casefold() for item in menu):
        print("An item with this name already exists.")
        return

    print("\nCategories:")

    for index, category in enumerate(CATEGORIES, 1):
        print(f"{index}. {category}")

    try:
        choice = int(input("Select Category: "))

        if not 1 <= choice <= len(CATEGORIES):
            print("Invalid category.")
            return

    except ValueError:
        print("Invalid choice.")
        return

    price = read_positive_number("Price: ₹")

    if price is None:
        return

    item = {
        "id": generate_id("FOOD"),
        "name": name,
        "category": CATEGORIES[choice - 1],
        "price": price,
        "available": True
    }

    menu.append(item)
    save_data(MENU_FILE, menu)

    print("Menu item added:", item["id"])


def view_menu():
    menu = load_data(MENU_FILE)

    if not menu:
        print("Menu is empty.")
        return

    print("\n========== RESTAURANT MENU ==========")

    for item in menu:
        print(
            f"{item['id']} | {item['name']} | "
            f"{item['category']} | {money(item['price'])} | "
            f"{'Available' if item['available'] else 'Unavailable'}"
        )


def update_menu_item():
    menu = load_data(MENU_FILE)

    item_id = input("Food ID: ").strip()
    item = find_by_id(menu, item_id)

    if not item:
        print("Menu item not found.")
        return

    new_price = input(
        f"New price [{item['price']}], Enter to skip: "
    ).strip()

    if new_price:
        try:
            price = float(new_price)

            if price <= 0:
                print("Price must be greater than zero.")
                return

            item["price"] = round(price, 2)

        except ValueError:
            print("Invalid price.")
            return

    availability = input(
        "Available? (y/n, Enter to skip): "
    ).strip().lower()

    if availability in ("y", "n"):
        item["available"] = availability == "y"
    elif availability:
        print("Invalid availability choice.")
        return

    save_data(MENU_FILE, menu)
    print("Menu item updated.")


def search_menu():
    keyword = input("Search food name: ").strip().casefold()

    if not keyword:
        print("Enter a search term.")
        return

    menu = load_data(MENU_FILE)

    results = [
        item for item in menu
        if keyword in item["name"].casefold()
    ]

    if not results:
        print("No matching items.")
        return

    for item in results:
        print(item["id"], item["name"], money(item["price"]))
