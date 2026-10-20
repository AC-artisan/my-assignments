# inventory.py - a product inentory system for a small store

inventory = {
    "laptop": {"price": 999.99, "quantity": 15},
    "mouse": {"price": 29.99, "quantity": 50},
    "monitor": {"price": 349.99, "quantity": 150},
    "keyboard": {"price": 139.99, "quantity": 75}
}

# display full inventory
def display_inventory():
    print("=" * 45)
    print("Store Product Inventory".center(45))
    print("=" * 45)
    print("\nPrice                             Items")

    for key, info in inventory.items():
        print(f"\n{info['price']} {info['quantity']:>30}")

# calculations
    laptop_value = float(inventory["laptop"]["price"] * inventory["laptop"]["quantity"])
    mouse_value = float(inventory["mouse"]["price"] * inventory["mouse"]["quantity"])
    monitor_value = float(inventory["monitor"]["price"] * inventory["monitor"]["quantity"])
    keyboard_value = float(inventory["keyboard"]["price"] * inventory["keyboard"]["quantity"])

    total_value = laptop_value + mouse_value + monitor_value + keyboard_value



# display total value of inventory, summed
    print("=" * 45)
    print(f"Total value: ${total_value:.2f}\n")
    print("-" * 45)


# display low stock items
    print("\nLow Stock Items (less than 10):")
    low_stock_items = {key: info for key, info in inventory.items() if info["quantity"] < 10}
    if low_stock_items:
        for key, info in low_stock_items.items():
            print(f"\n{key}: {info['quantity']} items")
    else:
        print("No low stock items.")


# look up a specific inventory item    
    search = input(f"\nSearch inventory - Please enter inventory item name: ")
    item = inventory.get(search)
    value = item.get("price") * item.get("quantity") if item else 0

    if item:
        print(f"\nFound: {search}") 
        print(f"Price: {item['price']}")
        print(f"Items: {item['quantity']}")
        print(f"{search} value: ${value:.2f}")

    else: print(f"No item found by that inventory name.")

    print("-" * 45)


# update quantities of an inventory item
    update = input(f"\nWould you like to update the quantity of an item? (y/n): ").lower()
    if update == "y": 
        item_name = input(f"\nPlease enter the inventory item name to update: ")
        item = inventory.get(item_name)
        if item:
            new_quantity = int(input(f"Enter new quantity for {item_name}: "))
            item["quantity"] = new_quantity
            print(f"\n{item_name} quantity updated to {new_quantity}.")
            print(f"\nUpdated Inventory:")
            display_inventory()

    if update == "n":
        print(f"\nNo updates made to inventory.")
        print(f"\nUpdated Inventory:")
        display_inventory()

    else:
        print(f"\nInvalid input.")


display_inventory()