# \n added to any str will print the following
# text on the next line
print("giggle")
print("boom\nwow\nbam\nkapow")
# this will also print the text on seperate lines
# but requires an extra print/more lines of code
print("giggle")
print("boom")
# cheese is the variable and "gouda" is the value of that variable
cheese = "gouda"
age = 5
print("cheese is " , cheese , ",aged " , age , "years")

name = "eric kogee"
print("hello", name ,"how are you?")
print(name.upper())
print(name.title())
print(name.lower())

quote = "famous quote by some dude"
dudes_name = "albert einstinian"
print(quote + " -" + dudes_name) # concatenated by a space and dash like a boss

# Define a variable
thing = "frog"
# print it 3 times
print(thing*3)
# End the code block

# Murica Baby!
print("=" * 14)
print(("||****========\n" *2).rstrip()) #.rstrip only removes whitespace at the end of a string
print(("||============"))               # it does not ifact remove whitespace from between two
print("=" * 14)                         # seperately printed strings on new lines
print("||\n" * 2)                       # .strip acts on left and right side of str

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

# this needs (,) to separate the str and int
age = 35
print("I am " , age , " years old")
# TypeError: can only concatenate(+) str (not "int") to str
# this is how you fix that error by converting the int to a str
#  using the str() function

age = 35
print("I am " + str(age) + " years old")

# age = 35
# print(f"I am" {age} "years old")

# f-strings (formatted string literals) this all must go inside
# a single set of quotes
# variables are placed inside the curly braces {}
# preceeded by the letter f
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

# this puts the divison last because of the parentheses
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
# -= will subtract from the original value
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

# this line will print the whole number solution
# to the equation
print(15 // 3)   # quotient
# this line will print the remainder
print(15 % 3)    # remainder
# this line will reverse the equation and end up at the
#original value of 15
print(3 * (15 // 3) + (15 % 3))
# more examples of printing results of divison
# and remainders
seats = 5
players = 23
print(players // seats)
print(players % seats)

# modulo means remainder. a modulo of two numbers 
# that are equal are congruent
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

# example of congruent numbers with the same modulo
print(64 % 5)
print(19 % 5)

# this converts the string "7" into the integer 7 
# this is called casting a string to an integer
number1 = int("7")
number2 = float("7")
print(number1)        # prints 7
print(type(number1))  # prints <class 'int'>
print(number2)        # prints 7.0
print(type(number2))  # prints <class 'float'>

# truncating numbers test
print(int(3.9))  # prints 3

# this will round but keep 2 decimal places
print(round(3.141159 ,2))  # prints 3.14
# this will just round the number and keep 0 decimal places
print(round(3.141159))     # prints 3
# this will round to 1 decimal place
# it rounds up and the next decimal place is zero
# 9.999 becomes 10.0
print (round(9.999, 1)) #<this prints 10.0>
# #this will round to 2 decimal places
print (round(9.999, 2)) #<this prints 10.0

# printing and rounding numbers
number = 9.999
rounded = round(9.999, 1)
print (round(9.999, 1))
print(rounded)
print(number)

coffee = 2.75
subtotal = coffee * 2
rounded_total = round(subtotal, 2)
print (rounded_total)

# .2f limits the number of decimal places to 2 
print(f"{rounded_total:.2f}")
# this is an f string that limits the number of decimal places to 2
print(f"{subtotal:.2f}")
total = 3.20
print(f"total: ${total:.2f}")

# more rounding examples
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

# input tracebacks and try/except blocks
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

# only accept numerical input from user
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

# error messasges
# SyntaxError (structure mistake)
# ZeroDivisionError (math rules)
# TypeError (mixed-up types)
# ValueError (bad value for a conversion)

# try/except blocks
# try:
    # risky code here
# except:
    # what to do on error

# example of try/except block
# how a real person would create this block vs chatgpt is astonishing
try:
    int(input("enter a number:"))
except:
    print("please enter a number")

# example of nested try/except blocks
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

# print debugging
price = 10
qty = 3
subtotal = price * qty
print("total:", subtotal)
print("price =", price, "qty =", qty)
print("subtotal =", subtotal)

print(f"price = {price}, qty = {qty}")
print(f"subtotal = {subtotal}")
# another way to format the print statement
price = 10
qty = 3
subtotal = price * qty
print("price =", price, "qty =", qty)
print("total:", subtotal)

# python treats all numbers as strings when inside the input form
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

# all of this is bad and wrong and wrong and bad
try:
    price = input("enter price: ")
    qty = input("enter quantity: ")
    totl = price * qty
    print("computing Total...")
    print("Total is", totl)
except:
    print("Something went wrong")

# fixed version of the bad and wrong code above
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

# defining parameters 
def greet(name):
    print("Hello", name)

# this is really cool
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

# more examples of defining functions with parameters
def area(w, h):
    area = int(w * h)
    print("Area equals: ", area)
area(5, 7)
area(2, 10)

# defining functions with no parameters prints both lines one after the other
def hello():
    print("hi")
    print("again")
hello()

# defining functions with parameters 
# calculating total with a discount
def checkout(price, qty):
    discount = .10          
    total = price * qty
    discounted_total = total - (total * discount)
    print(f"Total with discount: ${discounted_total:.2f}")
checkout(20, 3)

# adding banner
def banner(text, edge):
    print(edge * 3, text, edge * 3)
def greet(name):
    print(type(name))
    print("Hello", name)
banner("hello", "*")
greet("Cody")

# more examples of defining functions with parameters
def math(a, b):
    print("a =", a, "b =", b)
    print("result =", a - b)
    print("result =", a * b)
    print("result =", a / b)
    print("result =", a + b)
math(2, 5)

# check this out!
def subtract(a, b):
    print("a =", a, "b =", b)
    print("result =", a - b)
subtract(5, 2) 

# you have to have ":" at the end of the def line
# and the code block must be indented
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

# cleaner and neater way to format it 
def order(qty, price, item):
    print("qty =", qty, "price =", price, "item =", item)
    print(f"You ordered {qty} {item}, at ${price:.2f} each.")
    print(f"total: ${qty * price:.2f}")
order(2, 3, "tacos")

# using tuples
def add_subtract_multiply_divide(a, b):
    return(a + b, a - b, a * b, a / b)

answer = add_subtract_multiply_divide(5, 2)
print(answer)
double = answer * 2
print(double)

# unpacking tuples
def add_subtract_multiply_divide(a, b):
    return(a + b, a - b, a * b, a / b)

add, subtract, multiply, divide = add_subtract_multiply_divide(5, 2)
double = add, subtract, multiply, divide
print(add)
print(subtract)
print(multiply)
print(divide)
print(double)

# lists indexing, slicing
dog = "buddy"
print(dog[0])
print(dog[1])
print(dog[2])
fixed = "z" + dog[1:]
print(fixed)

# For somestring[start:stop:step]:
# Start: where you begin (includes this index)
# Stop: where you end (but not including this index)
# Step: how many you skip each time (defaults to 1)
dog = "buddy"
print(dog[1:4])
word = "happy"
print(word[0:5:2])

#ex [0:8:3] means start at index 0, stop before index 8, and take every 3rd character
word = "fantastic"
print(word[0:8:3])
print(word[1:8:3])
print(word[2:8:3])
print(word[3:8:3])
print(word[4:8:3])
print(word[5:8:3])
print(word[6:8:3])
print(word[7:8:3])
print(word[8:8:3])

# negative indexing
dog = "Beagle"
print(dog[-1])
print(dog[-2])
# rules of indexing apply in the same order
# but index values are reversed and go from right
# to left
pet = "parrot"
print(pet[-6], pet[-3], pet[-1])

event = "carnival"
time = "weekend"
print(event[2:7])
print(time[0:5])
print(event[-6:-1])
print(time[-7:-2])
# using number followed by colon 
# will print that letter followed by the remaining 
# letters after it ex n: alternatively 
# you can do :n to print the numbers
# preceeding it

# local variables indented lines are only defined
# and visible inside the demo function
# local variable examples
def add_tax(price):
    total = price * 1.1
    return(total)
#:::::: DEFINED FUNCTIONS MUST HAVE A COLON AFTER THEM ::::::
with_tax = add_tax(10)
add_tax(10)
print(with_tax)

def double(num):
    result = num * 2
    return(result)
doubled = double(5)
print(doubled)

#::::: YOU MUST HAVE A COLON AFTER DEFINING A FUNCTION :::::

#global variables
rate = 1.1
def add_tax(amount):
    return amount * rate

print(add_tax(10))

# variables outside of the local variable are called global 
# variables. They will not be used if a variable already exists
# inside the function.
# you can use 'global' to call the variable from outside of the 
# function instead
rate = 1.1
def hack():
    rate = 2      # local!
    return 10 * rate

print(hack())     # ?
print(rate)       # ?
# using global to call an outside variable into the def function
#
rate = 1.1
def change_rate():
    global rate
    rate = 2

change_rate()
print(rate)
# example
def game_shelf(games, shelves):
    return games / shelves

print(game_shelf(130, 4))
# example 
def final_price(tag, discount):
    return tag - (tag * discount)

print(final_price(50, 0.2))

# example of nested functions
def add_tax(amount):
    return amount * 1.1

def calc_total(price):
    return add_tax(price)

def checkout():
    total = calc_total(10)
    print(total)

def main():
    checkout()

# must add the () to call the main function
#main()
def add_tax(amount):
    return amount * 1.1
def total1(price):
    return add_tax(price)

def total2(price):
    return add_tax(price)

def main():
    print(total1(5))
    print(total2(10))

main()
# we call main at the end because python
# runs from top to bottom
# so if main was at the top it would not know
# what to call
# you could however define main() at the top
# as long as it is called last the code will still
# work top to bottom
# ----------------------------------------------------------
# calculating subtotal and total with tax and tip
# and formatting the output to 2 decimal places
# print(subtotal) prints the full number all decimal places
# print(f"${subtotal:.2f}") prints the number rounded to 2 decimal places
# this is called string formatting
# the underlying number is still the full number
# but the printed number is rounded to 2 decimal places
subtotal = 1.85*3 + 2.275*2
print(subtotal)
print(f"${subtotal:.2f}")

# do all your math first before asking for rounded number
# it could lose its precision
amount = 5.678
rounded = round(amount, 2)
print(rounded)
print(f"{rounded:.2f}")

# I get it but I don't think I rounded anything here?
def night_out(amount):
    return amount * 2

def ticket(price):
    return night_out(price)

def popcorn(price):
    return night_out(price)

def main():
    total = ticket(7.5) + popcorn(4.25)
    print(f"Total: ${total:.2f}")


main()

# this makes the field between | 6 spaces wide
# notice that .2f would add two decimal places
# so the total number of spaces is 6 including
# the decimal point and the two decimal places
print(f"|{123.4:6.2f}|")

# single print statement on two lines
print(f"|{3.5:6.2f}|\n|{123.4:6.2f}|")

# text alignment with f strings
# < left aligns
# > right aligns
# ^ center aligns
# the number is how many spaces wide the field is
print(f"|{'hi':<6}|")
print(f"|{'hi':>6}|")
print(f"|{'hi':^6}|")
print(f"|{'hello':<6}|")
print(f"|{'hello':>6}|")
print(f"|{'hello':^6}|")
print(f"|{'hello!':<6}|")

# example of formatting a receipt
item1, price1 = "cookie", 1.5
item2, price2 = "sandwich", 7.25
item3, price3 = "soda", 0.99
print(f"{item1:<10}    ${price1:>6.2f}\n{item2:<10}  ${price2:>6.2f}\n{item3:<10}    ${price3:>6.2f}")

# debugging with asserts and targeted prints
# assert tests if something is true
# if it is not true it will raise an error
def double(x):
   return x * 2

result = double(4)
assert result == 8, "double() is wrong"
print(double(4))
# how to use assert to check for zero values
# what you are checking comes after assert followed by , then error message
price = 1.25
qty   = 1
total = price * qty
assert total, "total must not equal zero"
print(f"total is ${total:.2f}") 

# setting assert to == (is equal to) will check that the assert is true and error if false
variable = 10
assert variable == 10, "variable does not equals 10"
print(variable)

# week one project for 
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

# remember to specify (type) before the input it does not have to be specified on the 
# def. 
def calc_total(price, quantity):
    return price * quantity

item1_name = input("enter name of item: ")
item1_price = float(input(f"enter price of {item1_name}: $"))
item1_quantity = int(input(f"enter quantity of {item1_name} "))

item_total = calc_total(item1_price, item1_quantity)

print(f": ${item_total:.2f}")

# --------------------------------------------WEEK TWO ----------------------------------------------
# if/else 
# notes from the reddit 
# https://docs.google.com/document/d/1hvW-N_bS_OwE_IhmxJh1PMyyvHr5XVkODPU23qA8kJE/edit?usp=sharing

for i in range(3):
    print("Brush teeth")

# Check if customer wants a drink – if/else
# Repeat for each snack ordered – loop
# Apply discount if total > $10 – if/else
# Print final bill – (neither, just output)

# start screen - output
# repeat until usr input == 'exit' - loop
# if 'new game', start new game - if/else
# if 'load game', load save file - if/else
# if 'options' open options menu - if/else
# if 'controls' open controls menu - if/else
# if 'exit' close options menu - if/else
# if 'exit game' end program - if/else

x = 10
if x > 5:
    print("big")
else:
    print("small")

answer = 'y'
if answer == 'y':
    print("yes!")
else:
    print("nope")

# using and/or with if/else
color = "green"
if color == "red" or color == "blue":
    print("allowed")
else:
    print("not allowed")

# not means the opposite so not false is true
print(5 > 3 and 2 > 1)
print(5 > 8 or 4 == 4)
print(not 7 < 2)

# if hot = false then it is not hot: print("wear a jacket")
hot = True
if not hot:
    print("wear a jacket")
else:
    print("t-shirt time")

# 
def right():
    print("right side ran")
    return True

print(False and right())
print(True or right())

# and/or and they must both be equally true or false, but or either one will be accepted
print(3 > 2 and 1 > 5) # false
print(2 == 3 or 4 < 5) # true (this is true because of (or), or is asking for either
                       # to be true not both)
print(not(9 > 7))      # false

# in python we don't use ! but it signifies (not) in other languages 
# since 2 = 2 is true (not) is checking to see if this statement is NOT false, aka true
print(not(2 != 2))

# 5 < 2 is False.
# not means “the opposite.”
# So, not(5 < 2) becomes not False.

# That’s the same as saying “it’s True that 5 is not less than 2.”

# So, not False = True.

# You can read not(5 < 2) like: “It’s not true that 5 is less than 2”—so, it’s true that it’s not!

# with and they both have to be true so for example
print(not(6 == 6 and 2 > 3)) # 6 == 6 is true, and 2 > 3 is false: therefor -
# "it is true that they are not both true so this is true." it is not false that they are bot not true
# it is infact true that they are both NOT true. there for this statement is true 

# it is false that this is not true. 
not(3 > 1 and (4 == 2 or 7 < 10))
    
# this prints True not flag
flag = True
print(flag)
    
# | If you mean...               | Use... |
# | ---------------------------- | ------ |
# | “Are these values the same?” | `==`   |
# | “Are these the same object?” | `is`   |
# is vs == you use == to compare equality, and is to compare object identity is the same

# True and False are special Boolean values.
# Use == to check if two values are equal (numbers, strings, etc).
# Use is only to check identity (like None, True, or False).
# For numbers or strings, always use == (not is).
# not flips a Boolean value, turning True to False and vice versa.

# if/elif/else in conjunction with in
text = "earn money fast!!!"
if "viagra" in text:
    print("spam")
elif "earn" in text:
    print("suspicious")
else:
    print("normal")
# using "if, elif, and else" statements in conjunction with "in"
movie = "R"
if "PG" in movie: 
    print("family")
elif "R" in movie: 
    print("adult")
else: 
    print("unknown")

message = "test@gmail.com"
if "@" in message and "." in message:
    print("looks like an email")
else: print("not an email")

message = "hey whats up?"
if "@" in message and "." in message:
    print("looks like an email")
else: print("not an email")

# too many if/else statments quickly make code harder to read
score = 92
if score >= 90:
    print("A")
elif score >= 60:
    print("B or C or D")
else:
    print("F")
if score >= 60:
    if score >= 90:
        print("A")
    else:
        print("B or C or D")
else:
    print("F")
# this is the same, we use elif to keep the code from becoming unreadable with too many if and else statements
score = 92
if score >= 90:
    print("A")
elif score >= 60:
    print("B or C or D")
else:
    print("F")

# proper if/elif/else statement
temp = 105
if temp >= 100:
    print("steam")
elif temp >= 0: 
    print("liquid")
else: print("ice")

temp = -5
if temp >= 100:
    print("steam")
elif temp >= 0:
    print("liquid")
else: print("ice")
# your narrowest ranges should come first in an if statement
score = 89
if score >= 90:
    print("A")
elif score >= 60:
    print("pass")
else:
    print("F")

# you must always repeat the variable when using (and)
weight = 55
if weight >= 50: 
    print("$25")
elif weight >= 10 and weight < 50:
    print("$10")
else: print("$5")

# more examples
weight = 12
if weight >= 50: 
    print("$25")
elif weight >= 10 and weight < 50:
    print("$10")
else: print("$5")

weight = 55
if weight >= 50: 
    print("$25")
elif weight >= 10 and weight < 50:
    print("$10")
else: print("$5")

print("python"[-3:])

# too many cats if/elif statement
cats = 15
if cats >= 20:
    print("holy crap thats a lot of cats")
elif cats <= 9:
    print("you should think about neutering")
else: 
    print("thats still too many cats")

cats = 9
if cats >= 15:
    print("holy cow thats a lot of cats")
elif cats <= 10:
    print("you should really think about neutering your cats")
else: 
    print("still too many cats")

print("cats"[0:3])


temp = 31
if temp < 32:
    print("freezing")
elif temp < 60:
    print("cold")
elif temp < 75:
    print("cool")
else:
    print("warm")

temp = 59
if temp < 32:
    print("freezing")
elif temp < 60:
    print("cold")
elif temp < 75:
    print("your mom")
else:
    print("i get it now")

weight = 19
if weight < 20:
    print("Standard")
elif weight < 10:
    print("Express")
elif weight < 5:
    print("Cheap")
else:
    print("Heavy")

weight = 9
if weight < 20:
    print("Standard")
elif weight < 10:
    print("Express")
elif weight < 5:
    print("Cheap")
else:
    print("Heavy")

weight = 4
if weight < 20:
    print("Standard")
elif weight < 10:
    print("Express")
elif weight < 5:
    print("Cheap")
else:
    print("Heavy")

# broader ranges go at the bottom, if 20 is at the top it will run first and never catch
# the more narrow range, every number below 20 will always trigger < 20 print statement
weight = 9
if weight < 5:
    print("Cheap")
elif weight < 10: 
    print("Express")
elif weight < 20:
    print("Standard")
else: print("Heavy")

# perfection
weight = 20
if weight >= 0 and weight <5:
    print("Cheap")
elif weight >= 5 and weight < 10: 
    print("Express")
elif weight >= 10 and weight < 20:
    print("Standard")
elif weight >= 20: #
    print("Heavy")
else: print("UNEXPECTED")

# loops/range
for i in range(5):
    print(i)
# i is just a placeholder/variable you can change it to anything

#start, stop 
for i in range(2, 6):
    print(i)
# value1 = start, value2 = stop, value3 = skip count
for i in range(5, -1, -1):
    print(i)

total = 0
for i in range(5):
    total += i
    print(total)
# or total after the loop just gives the final value
total = 0
for i in range(5):
    total += i
print(total)

# accumulation pattern adds the next sum in the range to i each loop
total = 0
for i in range(7):
    total += i
    print(total)
# if you wanted to start at 1, and end at 7. you would do 
total = 0
for i in range(1, 8):
    total += i
    print(total)

# ex. 2
for i in range(4, 21, 4):
    print(i)

# using modulo to find out if every number in the sequence is even
# i % 2 gives the remainder when dividing by 2.
# Even numbers divided by 2 have a remainder of 0.
for i in range(0, 11, 2):
    print(i, i % 2)

# countdown pattern
for i in range(5, -1, -1):
    print(i)

# accumulate sum of all values 
total = 0
for i in range(3, 31, 3):
    total += i
print(total)

# while loop and sentinel values
n = 0
while n < 3:
    print(n)
    n += 1 # removing this line will loop infinitately  

# modulo(%) = 1(odd) 0(even)
total = 0
num = int(input("Enter a number (-1 to stop): "))
while num != -1:
    total += num
    num = int(input("Enter a number (-1 to stop): "))
print("Total is:", total % 2)

# using str instead of int then adding up the total
count = 0
word = (input("Enter a word (stop to end): "))
while word != "stop":
    count += 1
    word = (input("Enter a word (stop to end): "))
print("Total is:", count)

# printing multiples of any number if n is divided by "7" with no remainder it has to be a multiple 
for n in range(1, 100):
    if n % 7 == 0:
        print(n)
# using fn + ins will enter OVERTYPE mode

# using break
for n in range(1, 21):
    print(n)
    if n % 7 == 0:
        break

# any number divided by 2 with a remainder of 0 is even, if the remainder is not 0 that number is odd
for n in range(1, 11):
    print(n)
    if n % 2 != 0:
        continue # if the remainder of n / 2 does NOT == 0 (!=0) continue to print
    print(n)

# break/continue example and defiintions we are checking for true/false value before moving on
for n in range(1, 16):
    if n % 4 == 0: # if the remainder of a number divided by 4 is equal to 0 = true so print if == 1 = false
        print("hit 4-multiple and break")
        break # terminate execution of innermost for/while loop if if branch = true break will run stopping
    # the entire loop immediately no further output will be given
    elif n % 2 ==0: # if the remainder of a number divided by 2 is equal to 0 print
        print(n)
        continue # skip remaining code in the for/while loop and proceed to next iteration ie: "else"
    else: 
        print("odd")

while True:
    try:
        num = int(input("Enter a number (1-10): "))
        if num < 1 or num > 10:
            print("Number must be between 1 and 10.")
            continue
        break
    except ValueError: # when code cannot convert value to int 
        print("That’s not a valid integer. Try again.")

print("You entered:", num)

# ValueError
while True:
    try:
        num = int(input("Enter a number (1-10): "))
        if num < 1 or num > 10:
            print("Number must be between 1 and 10.")
            continue
        break
    except ValueError: # everything is a str, only when you specify
        # int does it check for int in the input
        print("That’s not a valid integer. Try again.")

print("You entered:", num)

# any number divided by 2 and does not have a remainder of 0 is odd
while True: 
    try: 
        num = int(input("enter cost of item"))
        if num <= 0:
            print("must be positive number")
        elif num % 2 != 0: # modulo of n does NOT equal 0 then print
            print("must be even number")    
            continue
        break
    except ValueError: 
        print("valid numbers only")
print(f"you entered: ${num:.2f}")

# += means we are adding whatever the CURRENT value of n is 
total = 0
count = 0 
for n in range(3, 8):
    total += n
    count += 1
print(total, count)

for n in range(1, 11):
   if n % 2 != 0:
        continue # if the remainder of n / 2 does NOT == 0 (!=0) continue to print
print(n)

# I was overcomplicating this block by trying to find remainder when all
# I needed to do was skip count..
total = 0
count = 0 
for n in range(2, 11, 2):
    total += n
    count += 1
print(total, count)

# if n % 2 == 1 checks: “Is n odd?”
# When that’s true, the code inside the if block runs — here, adding to total and count.
# Nothing is automatically printed; the program only adds that odd n to your running total and count.
total = 0
count = 0
for n in range(1, 11):
    if n % 2 == 1: # 1 for odd number counting, 0 for even
        total += n # for these lines to be inside they must be indented 
        count += 1 # further
print(total, count)


# this was a doozy
min_num = None
max_num = None

while True:
    n = int(input("Enter a number (-1 to stop): "))
    if n == -1:
        break
    if min_num is None or n < min_num:
        min_num = n
    if max_num is None or n > max_num:
        max_num = n
print(min_num, max_num)


# this was so hard
min_num = None
max_num = None
total = 0
count = 0
while True:
    n = int(input("Enter a number (-1 to stop): "))
    if n == -1:
        break
    total += n 
    count += 1
    if min_num is None or n < min_num:
        min_num = n
    if max_num is None or n > max_num:
        max_num = n
    if count != 0:
        avg_num = total / count
    else:
        print("no numbers given")
print(f"{min_num}, {max_num}, {avg_num:.2f}")


# # practice with this
# ___ = None  # min_num
# ___ = None  # max_num
# ___ = 0     # total
# ___ = 0     # count

# while True:
#     n = int(input("Enter a number (-1 to stop): "))
#     if n == ___:  # what value stops the loop?
#         ___       # how do you break out?
#     ___ += n      # add to total
#     ___ += 1      # add to count

#     if ___ is None or n < ___:   # min check
#         ___ = n
#     if ___ is None or n > ___:   # max check
#         ___ = n

# if ___ != 0:                     # safe division
#     avg_num = ___ / ___
#     print(___, ___, f"{___:.2f}")
# else:
#     print("no numbers given")

# min_num = None  # min_num
# max_num = None  # max_num
# total = 0     # total
# count = 0     # count

# while True:
#     n = int(input("Enter a number (-1 to stop): "))
#     if n == -1:  # what value stops the loop?
#         break      # how do you break out?
#     total += n      # add to total
#     count += 1      # add to count

#     if min_num is None or n < min_num:   # min check
#         min_num = n
#     if max_num is None or n > max_num:   # max check
#         max_num = n

# if count != 0:                     # safe division
#     avg_num = total / count
#     print(max_num, min_num, f"{avg_num:.2f}")
# else:
#     print("no numbers given")

numbers = list(range(2, 11, 2))
print(numbers)
print(len(numbers))

scores = [80, 85, 90]
print(scores)
scores += [95] # adding to the list
print(scores)

fav_food = ["chinese food", "pizza", "spaghetti", "grilled chicken"]
fav_food += ["steak and eggs"] # adding to a list
print(len(fav_food)) # printing length of list
print(fav_food)

fav_food = ["chinese food", "pizza", "spaghetti", "grilled chicken"]
fav_food += ["steak and eggs"] # adding to a list
fav_food[2] = "lasagna" # repalacing item in a list
fav_food[3] = "ice cream" # individual replacement
fav_food[4] = "cake" 
fav_food[-2:] = ["ice cream", "cake"] # multiple replacment this is actually spot on the list
# "ice cream", "cake" would actually replace the string itself
print(len(fav_food)) # printing length of list
print(fav_food)
print(fav_food[1]) # 0 start indexing = lists start at 0 not 1 
print(fav_food[-1]) # prints last item in the list
print(fav_food[1:4])

nums = list(range(10))
print(nums)
print(nums[2:6]) # start at 2, end at 6 but not including 6


nums = list(range(10))
print(nums)
print(nums[:4])
print(nums[:3])    # numbers before index 3
print(nums[7:])    # numbers from index 7 to end
print(nums[:])     # full copy of nums
print(nums[-8:-2]) # start at 8 but excluding 8 listing backwards to 2 including 2
nums_copy = nums[:]
print(nums_copy is nums)
print(nums_copy, nums)

print("\tpython") # indentation with \t

print("Languages:\n\tPython\n\tC\n\tJavaScript") # \n new line \t indentation

# for loops are written like this
fav_food = ["pizza", "sushi", "ice cream"]
for food in fav_food:  # loop through each food in the list
    print(food)        # print the current food


fav_food = ["chinese food", "pizza", "spaghetti", "grilled chicken", "steak and eggs"]
for food in fav_food: # loops through the list
    for i in range(len(fav_food)): # numbering the list   
        print(i, fav_food[i]) # numbering the list
    print(f"I love {food}") # indented inside the loop

# enumeration numbering an index "i" for index 
# for "index", food in "enumerate" (fav_food)-list
fav_food = ["chinese food", "pizza", "spaghetti", "grilled chicken", "steak and eggs"]
for i, food in enumerate(fav_food):
    print(i, food) # numbers the list with enumerate unpacking the number and the food seperataly 
for food in fav_food: # loops through the list
    print(f"I love {food}") # indented inside the loop

fav_food = ["chinese food", "pizza", "spaghetti", "grilled chicken", "steak and eggs"]
for i, food in enumerate(fav_food):
    print(i + 1, food) # numbers the list with enumerate, adding 1 to start at 1 instead of 0
for food in fav_food: # loops through the list
    print(f"I love {food}") # indented inside the loop


# ENUMERATE NUMBERS THE LIST
# EXAMPLE OF ENUMERATION WITHOUT SPECIFYING AN INDEX VARIABLE eg: "i" or "food"
fav_food = ["chinese food", "pizza", "spaghetti", "grilled chicken", "steak and eggs"]
for food in enumerate(fav_food):
    print(food) # numbers the list with enumerate 
for food in fav_food: # loops through the list
    print(f"I love {food}") # indented inside the loop

# ENUMERATE NUMBERS THE LIST
# EXAMPLE OF ENUMERATION WITHOUT SPECIFYING AN INDEX VARIABLE eg: "i" or "food"
fav_food = ["chinese food", "pizza", "spaghetti", "grilled chicken", "steak and eggs"]
for food in enumerate(fav_food):
    print(food) # numbers the list with enumerate
for food in fav_food: # loops through the list
    print(f"I love {food}") # indented inside the loop

fav_food = ["chinese food", "pizza", "spaghetti", "grilled chicken", "steak and eggs"]
for i in enumerate(fav_food):
    print(i) # numbers the list with enumerate
for food in fav_food: # loops through the list
    print(f"I love {food}") # indented inside the loop

nums = [1, 3, 5, 7]
squares = []
for n in nums:
    squares += [n*n]
print(squares)

nums = [1, 3, 5, 7]
squares = []
for i, n in enumerate(nums):
    squares += [n*n]
print(squares)


nums = [6, 2, 9, 4]
for n in nums: 
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

# now THATS what I call for loop 2002 remix 
bitches = ["thick", "big tits", "pawg"]
for b in bitches:
    if b == "thick":
        print(f"{b} ya nigga dats my type")

for patient_awake in [True, False]:
    if patient_awake:
        print("Cook, Clean, Give medicine")
    else:
        print("Free time")

patient_awake = True
while patient_awake:
    print("Cook, Clean, Give medicine")
    patient_awake = False  # flip to asleep
print("Free time")

fav_food = ["pizza", "sushi", "tacos"]
for i, food in enumerate(fav_food):
    print(f"{i+1}. {food}")

for i, food in enumerate(fav_food, 1):
    print(f"{i}. {food}")

pets = ["dog", "cat"]
pets.append("parrot") # adding to the list
print(pets)

pets = ["dog", "cat", "parrot"]
pets.insert(1, "hamster")  # 1 is the index, "hamster" is the new item
print(pets)


pets = ["dog", "cat", "parrot"]
pets.remove("parrot") # remove from the list
print(pets)


pets = ["dog", "cat"]
gone = pets.pop(0) # pop removes and shows the item removed
print(gone)
for i, pets in enumerate(pets, 1):
    print(f"{i}. {pets}")

pets = ["dog", "cat"]
pets.extend(["parrot", "otter", "ferret"])
for i, pets in enumerate(pets, 1):
    print(i, pets)

# Use .extend() to add items one by one.
# Use .append() to add something as a single new element (even if it’s a list).

todo = ["laundry"]
todo.append("dishes") # add to the list
todo.append("clean") # add to the list, limited to one append at a time
todo.insert(0, "take medicine") # insert at index #
gone = todo.pop(3) # pop removes and shows the item removed
todo.remove("laundry") # removes the item in the list
todo.extend(["groceries", "call mom"]) # extends the list to include items at the end
print(gone)
for i, todo in enumerate(todo, 1): 
    print(i, todo)


















    

