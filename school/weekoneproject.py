# --------Receipt Calculator------- #
def calc_total(price:float, quantity:int):
    return price * quantity

def calc_grand_total(item1:float, item2:float):
    return item1 +  item2

item1_name = input(f"enter item name: ")
item1_price = float(input(f"enter price of {item1_name}: $"))
item1_quantity = int(input(f"enter quantity of {item1_name}: "))

item2_name = input(f"enter item name: ")
item2_price = float(input(f"enter price of {item2_name}: $"))
item2_quantity = int(input(f"enter quantity of {item2_name}: "))

item1_total = calc_total(item1_price, item1_quantity)
item2_total = calc_total(item2_price, item2_quantity)
total = calc_grand_total(item1_total, item2_total) 

print("\n----- RECEIPT -----")
print(f"{item1_name} x{item1_quantity} @ ${item1_price:>2.2f} = ${item1_total:>2.2f}")
print(f"{item2_name} x{item2_quantity} @ ${item2_price:>2.2f} = ${item2_total:>2.2f}")
print(f"Total: ${total:>2.2f}")



