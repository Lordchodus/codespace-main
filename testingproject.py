def calculate_total(price: float, quantity: int) -> float:
    """Returns the total price for an item."""
    return price * quantity

def calculate_grand_total(total1: float, total2: float) -> float:
    """Returns the grand total for both items."""
    return total1 + total2

# --- Input for Item 1 ---
item1_name = input("Enter name of first item: ")
item1_price = float(input(f"Enter price of {item1_name}: $"))
item1_quantity = int(input(f"Enter quantity of {item1_name}: "))

# --- Input for Item 2 ---
item2_name = input("Enter name of second item: ")
item2_price = float(input(f"Enter price of {item2_name}: $"))
item2_quantity = int(input(f"Enter quantity of {item2_name}: "))

# --- Calculations ---
item1_total = calculate_total(item1_price, item1_quantity)
item2_total = calculate_total(item2_price, item2_quantity)
grand_total = calculate_grand_total(item1_total, item2_total)

# --- Output (Receipt) ---
print("\n----- RECEIPT -----")
print(f"{item1_name} x{item1_quantity} @ ${item1_price:>2.2f} = ${item1_total:>2.2f}")
print(f"{item2_name} x{item2_quantity} @ ${item2_price:>2.2f} = ${item2_total:>2.2f}")
print(f"Grand Total: ${grand_total:>2.2f}")