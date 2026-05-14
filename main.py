# main.py - Main menu and program control

from models import Product, Vendor, PurchaseOrder
from file_manager import save_data, load_data
from inventory_manager import *
from reports import *
import datetime

def main():
    products, vendors, orders = load_data()
    
    while True:
        print("\n" + "="*50)
        print("      INVENTORY & PURCHASE ORDER SYSTEM")
        print("="*50)
        print("1. Product Management")
        print("2. Vendor Management")
        print("3. Create Purchase Order")
        print("4. Receive Shipment")
        print("5. Reports")
        print("6. Save Data")
        print("7. Exit")
        print("="*50)
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            product_menu(products)
        elif choice == "2":
            vendor_menu(vendors)
        elif choice == "3":
            create_po_menu(orders, products)
        elif choice == "4":
            po_num = input("PO Number: ").strip()
            receive_order(orders, products, po_num)
        elif choice == "5":
            report_menu(products, orders)
        elif choice == "6":
            save_data(products, vendors, orders)
        elif choice == "7":
            save_data(products, vendors, orders)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def product_menu(products):
    print("\n--- Product Management ---")
    print("1. Add Product")
    print("2. Edit Product")
    print("3. Deactivate Product")
    print("4. View All Products")
    print("5. Search by Name")
    print("6. Low Stock Report")
    ch = input("Choice: ").strip()
    if ch == "1": add_product(products)
    elif ch == "2": edit_product(products)
    elif ch == "3": deactivate_product(products)
    elif ch == "4": show_inventory(products)
    elif ch == "5":
        name = input("Enter name to search: ")
        results = search_by_name(products, name)
        for p in results: p.display()
    elif ch == "6": low_stock_report(products)


def vendor_menu(vendors):
    print("\nVendor Management - Basic (can be expanded)")
    print(f"Total Vendors: {len(vendors)}")


def create_po_menu(orders, products):
    po_number = input("PO Number: ").strip()
    vendor_id = input("Vendor ID: ").strip()
    items = []
    print("Add items (type 'done' when finished)")
    while True:
        pid = input("Product ID (or done): ").strip()
        if pid.lower() == "done":
            break
        try:
            qty = int(input("Quantity: "))
            prod = find_product(products, pid)
            price = prod.price if prod else float(input("Price: "))
            items.append({"pid": pid, "qty": qty, "price": price})
        except:
            print("Invalid input.")
    if items:
        order = PurchaseOrder(po_number, vendor_id, items, str(datetime.date.today()))
        orders.append(order)
        print("Purchase Order created successfully.")


def report_menu(products, orders):
    print("\n--- Reports ---")
    print("1. Full Inventory")
    print("2. Low Stock")
    print("3. Total Value")
    print("4. Category Report")
    print("5. Open Orders")
    ch = input("Choice: ").strip()
    if ch == "1": show_inventory(products)
    elif ch == "2": low_stock_report(products)
    elif ch == "3": total_value_report(products)
    elif ch == "4": category_report(products)
    elif ch == "5": open_orders_report(orders)


if __name__ == "__main__":
    main()