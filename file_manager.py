# file_manager.py - Handles saving and loading data

import json
from models import Product, Vendor, PurchaseOrder

def save_data(products, vendors, orders, filename="data.json"):
    """Save all data to JSON file."""
    data = {
        "products": [p.to_dict() for p in products],
        "vendors": [v.to_dict() for v in vendors],
        "orders": [o.to_dict() for o in orders]
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print("Data saved successfully.")


def load_data(filename="data.json"):
    """Load data from JSON file."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        
        products = [Product(**p) for p in data.get("products", [])]
        vendors = [Vendor(**v) for v in data.get("vendors", [])]
        orders = [PurchaseOrder(**o) for o in data.get("orders", [])]
        
        print(f"Loaded {len(products)} products, {len(vendors)} vendors, {len(orders)} orders.")
        return products, vendors, orders
    except FileNotFoundError:
        print("No data file found. Starting fresh.")
        return [], [], []
    except Exception as e:
        print(f"Error loading data: {e}")
        return [], [], []