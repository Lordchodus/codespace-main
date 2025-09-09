def calc_total(price, quantity):
    return price * quantity

item1_name = input("enter name of item: ")
item1_price = float(input(f"enter price of {item1_name}: $"))
item1_quantity = int(input(f"enter quantity of {item1_name} "))

item_total = calc_total(item1_price, item1_quantity)

print(f": ${item_total:.2f}")
