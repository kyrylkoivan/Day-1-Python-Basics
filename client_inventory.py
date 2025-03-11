"""
Client Inventory Management Script
----------------------------------
This script manages a nested dictionary mimicking a client inventory (e.g., an electronic store).
It provides functions to:
- Count total inventory items
- Identify low-stock items below a threshold
- Process orders and update stock levels


Author: [Your Name]
"""

# Sample Inventory Data (Nested Dictionary Format)
inventory = {
    "Laptops": {
        "Dell XPS 13": {"stock": 10, "price": 1200},
        "MacBook Pro 14": {"stock": 5, "price": 2000},
        "Lenovo ThinkPad X1": {"stock": 7, "price": 1500},
    },
    "Smartphones": {
        "iPhone 14": {"stock": 15, "price": 999},
        "Samsung Galaxy S23": {"stock": 12, "price": 850},
        "Google Pixel 7": {"stock": 8, "price": 799},
    },
    "Tablets": {
        "iPad Pro": {"stock": 6, "price": 1100},
        "Samsung Galaxy Tab S8": {"stock": 9, "price": 750},
    },
}


def count_total_items(inventory):
    """Counts total items in all categories."""
    return sum(item["stock"] for category in inventory.values() for item in category.values())


def find_low_stock_items(inventory, threshold=5):
    """Finds items with stock below a given threshold."""
    low_stock = {}
    for category, items in inventory.items():
        for item, details in items.items():
            if details["stock"] < threshold:
                low_stock.setdefault(category, {})[item] = details["stock"]
    return low_stock


def process_order(inventory, category, item, quantity):
    """
    Processes a simulated order:
    - Checks stock availability
    - Updates inventory if stock is sufficient
    """
    if category in inventory and item in inventory[category]:
        if inventory[category][item]["stock"] >= quantity:
            inventory[category][item]["stock"] -= quantity
            return f"Order successful! {quantity} {item}(s) processed."
        else:
            return f"Insufficient stock for {item}. Only {inventory[category][item]['stock']} left."
    return f"Item '{item}' not found in category '{category}'."


# Main execution for testing functions
if __name__ == "__main__":
    print("Total items in inventory:", count_total_items(inventory))
   
    low_stock_items = find_low_stock_items(inventory, threshold=5)
    print("\nLow stock items (below threshold 5):", low_stock_items)
   
    print("\nProcessing order for 3 MacBook Pro 14...")
    print(process_order(inventory, "Laptops", "MacBook Pro 14", 3))
   
    print("\nProcessing order for 10 iPhone 14 (should fail due to stock)...")
    print(process_order(inventory, "Smartphones", "iPhone 14", 10))

    print("\nUpdated Inventory:", inventory)