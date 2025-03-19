"""
Client Inventory Management Script (Refactored)
----------------------------------------------
Modular version with reusable functions.
"""

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
    return sum(item["stock"] for category in inventory.values() for item in category.values())

def find_low_stock_items(inventory, threshold=5):
    return {
        category: {item: details["stock"] for item, details in items.items() if details["stock"] < threshold}
        for category, items in inventory.items()
        if any(details["stock"] < threshold for details in items.values())
    }

def process_order(inventory, category, item, quantity):
    if category in inventory and item in inventory[category]:
        stock = inventory[category][item]["stock"]
        if stock >= quantity:
            inventory[category][item]["stock"] -= quantity
            return f"Order successful: {quantity} {item}(s) processed."
        return f"Insufficient stock for {item}. Only {stock} left."
    return f"Item '{item}' not found in category '{category}'."

def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for category, items in inventory.items():
        print(f"\nCategory: {category}")
        for item, details in items.items():
            print(f"  {item}: Stock={details['stock']}, Price=${details['price']}")

def main():
    print("Total items in inventory:", count_total_items(inventory))
    display_inventory(inventory)
    print("\nLow stock items:", find_low_stock_items(inventory, threshold=5))
    print("\n", process_order(inventory, "Laptops", "MacBook Pro 14", 3))
    print(process_order(inventory, "Smartphones", "iPhone 14", 10))
    display_inventory(inventory)

if __name__ == "__main__":
    main()