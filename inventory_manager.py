# inventory_manager.py - Core functions for inventory and orders

from models import Product

def add_product(products):
    """Add a new product to inventory."""
    pid = input("Product ID: ").strip()
    if any(p.pid == pid for p in products):
        print("Error: Product ID already exists.")
        return
    name = input("Name: ").strip()
    category = input("Category: ").strip()
    try:
        qty = int(input("Quantity: "))
        rlevel = int(input("Reorder Level: "))
        rqty = int(input("Reorder Quantity: "))
        price = float(input("Price: "))
    except ValueError:
        print("Error: Invalid number entered.")
        return
    vid = input("Vendor ID: ").strip()

    products.append(Product(pid, name, category, qty, rlevel, rqty, price, vid))
    print("Product added successfully.")


def edit_product(products):
    """Edit an existing product."""
    pid = input("Enter Product ID to edit: ").strip()
    prod = find_product(products, pid)
    if not prod:
        print("Product not found.")
        return
    prod.name = input(f"New name ({prod.name}): ") or prod.name
    prod.category = input(f"New category ({prod.category}): ") or prod.category
    print("Product updated.")


def deactivate_product(products):
    """Deactivate a product."""
    pid = input("Enter Product ID to deactivate: ").strip()
    prod = find_product(products, pid)
    if prod:
        prod.active = False
        print("Product deactivated.")
    else:
        print("Product not found.")


def find_product(products, pid):
    """Find product by ID."""
    for p in products:
        if p.pid == pid:
            return p
    return None


def search_by_name(products, name):
    """Search products by name."""
    return [p for p in products if name.lower() in p.name.lower()]


def search_by_category(products, category):
    """Search products by category."""
    return [p for p in products if p.category.lower() == category.lower()]


def search_by_vendor(products, vendor_id):
    """Search products by vendor ID."""
    return [p for p in products if p.vendor_id == vendor_id]


def sort_by_name(products):
    """Sort products by name."""
    return sorted(products, key=lambda p: p.name)


def sort_by_quantity(products):
    """Sort products by quantity."""
    return sorted(products, key=lambda p: p.quantity)


def sort_by_price(products):
    """Sort products by price."""
    return sorted(products, key=lambda p: p.price)


def receive_order(orders, products, po_number):
    """Receive shipment and update inventory."""
    for order in orders:
        if order.po_number == po_number:
            if order.status == "received":
                print("This order was already received.")
                return
            for item in order.items:
                prod = find_product(products, item["pid"])
                if prod:
                    prod.quantity += item["qty"]
            order.status = "received"
            print("Shipment received and inventory updated.")
            return
    print("Order not found.")