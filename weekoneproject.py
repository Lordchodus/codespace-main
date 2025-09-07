def calculate_total(price, quantity):
    return price * quantity

def calculate_grand_total(total1, total2):
    return total1 + total2

item1_name = input("Enter item name: ")
item1_price = (input(f"Enter price of {item1_name}: $"))
item1_quantity = (input(f"Enter quantity of {item1_name}: "))

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
