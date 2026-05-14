# reports.py - All reporting functions

def show_inventory(products):
    """Display full inventory."""
    print("\n=== FULL INVENTORY ===")
    for p in products:
        if p.active:
            p.display()


def low_stock_report(products):
    """Display low stock items."""
    print("\n=== LOW STOCK REPORT ===")
    found = False
    for p in products:
        if p.quantity <= p.reorder_level and p.active:
            p.display()
            found = True
    if not found:
        print("No low stock items.")


def total_value_report(products):
    """Show total inventory value."""
    total = sum(p.quantity * p.price for p in products if p.active)
    print(f"\nTotal Inventory Value: ${total:,.2f}")


def category_report(products):
    """Show products count by category."""
    print("\n=== CATEGORY REPORT ===")
    from collections import Counter
    cats = Counter(p.category for p in products if p.active)
    for cat, count in sorted(cats.items()):
        print(f"{cat}: {count} products")


def open_orders_report(orders):
    """Show open purchase orders."""
    print("\n=== OPEN PURCHASE ORDERS ===")
    open_list = [o for o in orders if o.status == "open"]
    if not open_list:
        print("No open orders.")
        return
    for o in open_list:
        print(f"PO #{o.po_number} | Vendor: {o.vendor_id} | Total: ${o.total:.2f}")