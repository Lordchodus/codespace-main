def calc_total(price:float, quantity):
    return price * quantity

def calc_grand_total(total1:float, total2:float):
    return total1 + total2

item1_name = input(f"enter item name: ")
item1_price = float(input(f"enter price of {item1_name}: $"))
item1_quantity = int(input(f"enter quantity of {item1_name}: "))

item2_name = input(f"enter item name: ")
item2_price = float(input(f"enter price of {item2_name}: $"))
item2_quantity = int(input(f"enter quantity of {item2_name}: "))

item1_total = calc_total(item1_price, item1_quantity)
item2_total = calc_total(item2_price, item2_quantity)
total = calc_grand_total(item1_total, item2_total) 



