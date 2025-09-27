
# conversion calculator
while True:
    try:
        weight = int(input("Enter your weight: "))
        break
    except ValueError:
        print("whole number only")
    
while True:         
        unit = input("kilograms or pounds (k or l): ")
        if unit in ["k", "l"]:
            break
        else:
            print("enter 'k' or 'l'")

if unit == "k":
    weight = weight * 2.205
    unit = "lbs"
elif unit == "l":
    weight = weight / 2.205
    unit = "kgs"
else: 
    print(f"{unit} was not valid")

print(f"your weight is: {weight:.2f} {unit}")