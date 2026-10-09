from menu_manager import (
    add_menu_item,
    view_menu,
    update_menu_item,
    search_menu
)

from customer_manager import (
    add_customer,
    view_customers,
    search_customer
)

from order_manager import (
    create_order,
    view_orders,
    search_order,
    update_order_status
)

from payment_manager import (
    record_payment,
    view_payments
)

from report_manager import (
    sales_report,
    popular_items_report,
    pending_payment_report
)


def main():
    actions = {
        "1": add_menu_item,
        "2": view_menu,
        "3": update_menu_item,
        "4": search_menu,
        "5": add_customer,
        "6": view_customers,
        "7": search_customer,
        "8": create_order,
        "9": view_orders,
        "10": search_order,
        "11": update_order_status,
        "12": record_payment,
        "13": view_payments,
        "14": sales_report,
        "15": popular_items_report,
        "16": pending_payment_report
    }

    while True:
        print("\n" + "=" * 48)
        print("      RESTAURANT ORDER MANAGEMENT")
        print("=" * 48)

        options = [
            "Add Menu Item",
            "View Menu",
            "Update Menu Item",
            "Search Menu",
            "Add Customer",
            "View Customers",
            "Search Customer",
            "Create Order",
            "View Orders",
            "Search Order",
            "Update Order Status",
            "Record Payment",
            "View Payments",
            "Today's Sales Report",
            "Popular Items Report",
            "Pending Payment Report"
        ]

        for number, option in enumerate(options, 1):
            print(f"{number}. {option}")

        print("0. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "0":
            print("Thank you for using the system!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (OSError, RuntimeError) as error:
                print("Storage error:", error)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
