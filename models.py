# models.py - 

class Product:
    """Represents a product in the inventory."""
    def __init__(self, pid, name, category, quantity, reorder_level, 
                 reorder_qty, price, vendor_id):
        self.pid = pid
        self.name = name
        self.category = category
        self.quantity = int(quantity)
        self.reorder_level = int(reorder_level)
        self.reorder_qty = int(reorder_qty)
        self.price = float(price)
        self.vendor_id = vendor_id
        self.active = True

    def to_dict(self):
        return self.__dict__

    def display(self):
        status = "Active" if self.active else "Inactive"
        print(f"{self.pid} | {self.name} | {self.category} | Stock: {self.quantity} | ${self.price:.2f} | {status}")


class Vendor:
    """Represents a vendor/supplier."""
    def __init__(self, vid, name, contact, phone, email, address):
        self.vid = vid
        self.name = name
        self.contact = contact
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self):
        return self.__dict__


class PurchaseOrder:
    """Represents a purchase order."""
    def __init__(self, po_number, vendor_id, items, date_created, status="open"):
        self.po_number = po_number
        self.vendor_id = vendor_id
        self.items = items
        self.date_created = date_created
        self.status = status
        self.total = sum(item["qty"] * item["price"] for item in items)

    def to_dict(self):
        return self.__dict__