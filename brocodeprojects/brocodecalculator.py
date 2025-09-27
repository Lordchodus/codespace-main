import math

while True:
    operator = input("Enter an operator (+ - * /): ")
    if operator in ["+", "-", "*", "/"]:
        break
    else: print("Not a valid operator")

num1 = float(input("Enter first number: "))
num2 = float(input("enter second number: ")) 

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print(f"{operator} is not a valid operator")
    result = None

if result is not None:
    print(f"{result:.2f}")