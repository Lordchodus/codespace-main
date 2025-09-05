# \n added to any str will print the following
# text on the next line
print("giggle")
print("boom\nwow")
# this will also print the text on seperate lines
# but requires an extra print/more lines of code
print("giggle")
print("boom")
# cheese is the variable and "gouda" is the value of that variable
cheese = "gouda"
age = 5
print("cheese is " , cheese , ",aged " , age , "years")

#Define a variable
thing = "frog"
#print it 3 times
print(thing*3)
#End the code block

#Murica Baby!
print("=" * 14)
print(("||****========\n" *2).rstrip())
print(("||============"))
print("=" * 14)
print("||\n" * 2)

waffles = 42
print(type(waffles))
waffles = "delicious"
print(type(waffles))

waffles = 42
print(type(waffles))
waffles = "delicious"
print(type(waffles))

print('She said "hi"\\"bye"')

color = "blue"
animal = "duck"
# + joins strings together and * repeats them
tag = color + animal
print(tag*3)

#this needs (,) to separate the str and int
age = 25
print("I am " , age , " years old")
# TypeError: can only concatenate(+) str (not "int") to str
# this is how you fix that error by converting the int to a str
#  using the str() function

age = 25
print("I am " + str(age) + " years old")

# age = 25
# print(f"I am" {age} "years old")

# f-strings (formatted string literals) this all must go inside
# a single set of quotes
# variables are placed inside the curly braces {}
#preceeded by the letter f
age = 25
print(f"I am {age} years old")

age = 35
gpa = 4.0
pet = "cat"

print(f"I am {age} years old, my gpa is {gpa}, and I have a pet {pet}.")

print(2 + 3 * 4) # prints 14 not 20 because of order of operations
print((2 + 3) * 4) # prints 20 because of parentheses

# print(10-6/2) 7.0 # prints 7.0
# print((10-6)/2) 2.0 # prints 2.0
# #division will always give a float

print(5 + 2 * 3 - 1)
# the parentheses change the order of operations
print((5 + 2) * (3 - 1))

#this puts the divison last because of the parentheses
print(8 / (4 + 2 * 3))

# this is how you ignore PEMDAS by using parenthesis to calculate whats inside first
price = 20
tax = 0.07
tip = 3
print(price + price * tax + tip)
print((price + tip) * tax + price)

# this is how you add value's to the variable you are calling
wallet = 10
wallet = wallet + 5
print("wallet now:", wallet)
# += will add to the original value
steps = 0
steps += 100
print(steps)

steps += 100
print("after +=", steps)

budget = 50
budget -= 12
print("left:", budget)

calories = 2000
print(calories)
calories -= 500
print(calories)
calories -= 500
print(f"You burned",calories,"calories")

cups = 0
cups += 1   # morning
print("after breakfast", cups, "cup(s)")
cups += 1   # afternoon refill
print("total so far", cups, "cup(s)")
cups -= 1   # spilled one 😅
print("oops, now only", cups, "cup(s)")

# floor division will round down and drop the decimal point
# turns a float into a whole integer
print(7//2)

# this will print the remainder leftover after the division
# so 5 goes into 17 3 times wit 2 leftover
print(17%5)

print(5 * (5 // 2) + (5 % 2))

#this line will print the whole number solution
#to the equation
print(15 // 3)   # quotient
#this line will print the remainder
print(15 % 3)    # remainder
#this line will reverse the equation and end up at the
#original value of 15
print(3 * (15 // 3) + (15 % 3))
#more examples of printing results of divison
# and remainders
seats = 5
players = 23
print(players // seats)
print(players % seats)

#modulo means remainder. a modulo of two numbers 
#that are equal are congruent
print(56 % 7)
print((56 + 7) % 7)

# imagine a 12 hour clock if its 9 o clock
# and you add 7 hours that equals 4 o clock
# this line is how you use modulo to show that
# this takes the current value of 9, adds 7 to it
# then shows the remainder of 16 // (divided by) 12
# which is a remainder of 4
print((9 + 7) % 12)


stacys_mom = "got it goin on"
waited = "for so long"
print(f"stacey's mom has",stacys_mom,"she's all I want and I've",waited,)

#example of congruent numbers with the same modulo
print(64 % 5)
print(19 % 5)

# this converts the string "7" into the integer 7 
#this is called casting a string to an integer
number1 = int("7")
number2 = float("7")
print(number1)        # prints 7
print(type(number1))  # prints <class 'int'>
print(number2)        # prints 7.0
print(type(number2))  # prints <class 'float'>

#truncating numbers test
print(int(3.9))  # prints 3

#this will round but keep 2 decimal places
print(round(3.141159 ,2))  # prints 3.14
#this will just round the number and keep 0 decimal places
print(round(3.141159))     # prints 3
#this will round to 1 decimal place
#it rounds up and the next decimal place is zero
#9.999 becomes 10.0
print (round(9.999, 1)) #<this prints 10.0>
# #this will round to 2 decimal places
print (round(9.999, 2)) #<this prints 10.0

#printing and rounding numbers
number = 9.999
rounded = round(9.999, 1)
print (round(9.999, 1))
print(rounded)
print(number)

coffee = 2.75
subtotal = coffee * 2
rounded_total = round(subtotal, 2)
print (rounded_total)

#.2f limits the number of decimal places to 2 
print(f"{rounded_total:.2f}")
#this is an f string that limits the number of decimal places to 2
print(f"{subtotal:.2f}")
total = 3.20
print(f"total: ${total:.2f}")

#more rounding examples
print(float(3.2))
print(round(3.2, 2))
print(f"{3.2:.2f}")
# more formatting examples of rounding to 2 decimal places
print(f"item: ${1.99:.2f}")
print(f"item: ${2.5:.2f}")
print(f"item: ${3.455:.2f}")

soda = 1.85 * 3
snacks = 2.275 * 2
total = soda + snacks
print(f"final total: ${total:.2f}")

#input tracebacks and try/except blocks
input("how many coffees? ")
# all input is a str even numbers
response = input("how many coffees? ")
print(response)
print(type(response))

# converting str to int for math
count = int(input("how many coffee?"))
price = 2.75
total = count * price
print(f"total: ${total:.2f}")

#only accept numerical input from user
def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            # Attempt to convert to an integer
            value = int(user_input)
            return value
        except ValueError:
            try:
                # If integer conversion fails, attempt to convert to a float
                value = float(user_input)
                return value
            except ValueError:
                print("Invalid input. Please enter a number.")

# Example usage:
age = get_numeric_input("Enter your age: ")
print(f"Your age is: {age}")

price = get_numeric_input("Enter the price: ")
print(f"The price is: {price:.2f}")

#error messasges
# SyntaxError (structure mistake)
# ZeroDivisionError (math rules)
# TypeError (mixed-up types)
# ValueError (bad value for a conversion)

#try/except blocks
#try:
    # risky code here
#except:
    # what to do on error

#example of try/except block
#how a real person would create this block vs chatgpt is astonishing
try:
    int(input("enter a number:"))
except:
    print("please enter a number")

#example of nested try/except blocks
try:
    price = float(input("enter the price: "))
except:
    print("please enter a valid price")
else:
    try:
        quantity = int(input("enter the quantity: "))
    except:
        print("please enter a valid quantity")
    else:
        total = price * quantity
        print(f"total: ${total:,.2f}")
# you can also use a comma to denote the thousands place

#print debugging
price = 10
qty = 3
subtotal = price * qty
print("total:", subtotal)
print("price =", price, "qty =", qty)
print("subtotal =", subtotal)

print(f"price = {price}, qty = {qty}")
print(f"subtotal = {subtotal}")
#another way to format the print statement
price = 10
qty = 3
subtotal = price * qty
print("price =", price, "qty =", qty)
print("total:", subtotal)

#python treats all numbers as strings when inside the input form
cups = input("cups? ")
print("raw cups =", cups, type(cups))
cups = int(cups)
print("after int, cups =", cups, type(cups))
total = cups * 2.5
print(f"total: ${total:,.2f}")

# except = what to do when there’s an error
# else = what to do only if everything in try worked fine


try:
    price = 10
    qty = 3
    totl = price * qty
    print("computing Total...")
    print("Total is", totl)
except:
    print("Something went wrong")

#all of this is bad and wrong and wrong and bad
try:
    price = input("enter price: ")
    qty = input("enter quantity: ")
    totl = price * qty
    print("computing Total...")
    print("Total is", totl)
except:
    print("Something went wrong")

#fixed version of the bad and wrong code above
try:
    raw_price = input("Item Price: ")
    print("User typed price:", raw_price)
    price = float(raw_price)
    print(f"Price (float): {price:.2f}")
    print("price =", price, type(price))

    raw_qty = input("Quantity: ")
    print("User typed quanitity:", raw_qty)
    qty = int(raw_qty)
    print("Quantity =", qty, type(qty))
    
    total = price * qty
    print("Computing Total")
    print(f"Total: ${total:.2f}")
except:
    print("Please enter a valid price and quantity")

#defining parameters 
def greet(name):
    print("Hello", name)

#this is really cool
name = input("Enter your name: ")
def greet(name):
    print(type(name))
    print("Hello", name)
greet(name)

# using variables to call def functions
cost = 12
number = 5
def total(price, qty):
    qty = int(qty)
    print("Total is $", price * qty)
total(cost, number)

#more examples of defining functions with parameters
def area(w, h):
    area = int(w * h)
    print("Area equals: ", area)
area(5, 7)
area(2, 10)

#defining functions with no parameters prints both lines one after the other
def hello():
    print("hi")
    print("again")
hello()

#defining functions with parameters 
#calculating total with a discount
def checkout(price, qty):
    discount = .10          
    total = price * qty
    discounted_total = total - (total * discount)
    print(f"Total with discount: ${discounted_total:.2f}")
checkout(20, 3)

#adding banner
def banner(text, edge):
    print(edge * 3, text, edge * 3)
def greet(name):
    print(type(name))
    print("Hello", name)
banner("hello", "*")
greet("Cody")

#more examples of defining functions with parameters
def math(a, b):
    print("a =", a, "b =", b)
    print("result =", a - b)
    print("result =", a * b)
    print("result =", a / b)
    print("result =", a + b)
math(2, 5)

#check this out!
def subtract(a, b):
    print("a =", a, "b =", b)
    print("result =", a - b)
subtract(5, 2) 

#you have to have ":" at the end of the def line
#and the code block must be indented
def tacos(qty, price):
    print(f"You ordered {qty} tacos at ${price:.2f} each.")
    print(f"total: ${qty * price:.2f}")
tacos(2, 3)

# this is actually super interesting way to call a function
# you can call the parameters in any order as long as a str is in quotes in the call
def order(qty, price, item):
    print(f"You ordered {qty} {item}, at ${price:.2f} each.")
    print(f"total: ${qty * price:.2f}")
    print("qty =", qty, "price =", price, "item =", item)
order(2, 3, "tacos")

#cleaner and neater way to format it 
def order(qty, price, item):
    print("qty =", qty, "price =", price, "item =", item)
    print(f"You ordered {qty} {item}, at ${price:.2f} each.")
    print(f"total: ${qty * price:.2f}")
order(2, 3, "tacos")