# # \n added to any str will print the following
# # text on the next line
# print("giggle")
# print("boom\nwow")
# # this will also print the text on seperate lines
# # but requires an extra print/more lines of code
# print("giggle")
# print("boom")
# # cheese is the variable and "gouda" is the value of that variable
# cheese = "gouda"
# age = 5
# print("cheese is " , cheese , ",aged " , age , "years")

# #Define a variable
# thing = "frog"
# #print it 3 times
# print(thing*3)
# #End the code block

#Murica Baby!
print("=" * 14)
print(("||****========\n" *2).rstrip())
print(("||============"))
print("=" * 14)
print("||\n" * 2)

# waffles = 42
# print(type(waffles))
# waffles = "delicious"
# print(type(waffles))

# waffles = 42
# print(type(waffles))
# waffles = "delicious"
# print(type(waffles))

# print('She said "hi"\\"bye"')

# color = "blue"
# animal = "duck"
# # + joins strings together and * repeats them
# tag = color + animal
# print(tag*3)

# age = 25
# print("I am " + age + " years old")
# # TypeError: can only concatenate str (not "int") to str

# age = 25
# print("I am " + str(age) + " years old")

# # age = 25
# # print(f"I am" {age} "years old")

# # f-strings (formatted string literals) this all must go inside
# # a single set of quotes
# # variables are placed inside the curly braces {}
# #preceeded by the letter f
# age = 25
# print(f"I am {age} years old")

# age = 35
# gpa = 4.0
# pet = "cat"

# print(f"I am {age} years old, my gpa is {gpa}, and I have a pet {pet}.")

# print(2 + 3 * 4) # prints 14 not 20 because of order of operations
# print((2 + 3) * 4) # prints 20 because of parentheses

# # print(10-6/2) 7.0 # prints 7.0
# # print((10-6)/2) 2.0 # prints 2.0
# # #division will always give a float

# print(5 + 2 * 3 - 1)
# # the parentheses change the order of operations
# print((5 + 2) * (3 - 1))

# #this puts the divison last because of the parentheses
# print(8 / (4 + 2 * 3))

# # this is how you ignore PEMDAS by using parenthesis to calculate whats inside first
# price = 20
# tax = 0.07
# tip = 3
# print(price + price * tax + tip)
# print((price + tip) * tax + price)

# # this is how you add value's to the variable you are calling
# wallet = 10
# wallet = wallet + 5
# print("wallet now:", wallet)
# # += will add to the original value
# steps = 0
# steps += 100
# print(steps)

# steps += 100
# print("after +=", steps)

# budget = 50
# budget -= 12
# print("left:", budget)

# calories = 2000
# print(calories)
# calories -= 500
# print(calories)
# calories -= 500
# print(f"You burned",calories,"calories")

# cups = 0
# cups += 1   # morning
# print("after breakfast", cups, "cup(s)")
# cups += 1   # afternoon refill
# print("total so far", cups, "cup(s)")
# cups -= 1   # spilled one 😅
# print("oops, now only", cups, "cup(s)")

# # floor division will round down and drop the decimal point
# # turns a float into a whole integer
# print(7//2)

# # this will print the remainder leftover after the division
# # so 5 goes into 17 3 times wit 2 leftover
# print(17%5)

# print(5 * (5 // 2) + (5 % 2))

# #this line will print the whole number solution
# #to the equation
# print(15 // 3)   # quotient
# #this line will print the remainder
# print(15 % 3)    # remainder
# #this line will reverse the equation and end up at the
# #original value of 15
# print(3 * (15 // 3) + (15 % 3))
# #more examples of printing results of divison
# # and remainders
# seats = 5
# players = 23
# print(players // seats)
# print(players % seats)

# modulo
# print(56 % 7)
# print((56 + 7) % 7)

# # imagine a 12 hour clock if its 9 o clock
# # and you add 7 hours that equals 4 o clock
# # this line is how you use modulo to show that
# # this takes the current value of 9, adds 7 to it
# # then shows the remainder of 16 // (divided by) 12
# # which is a remainder of 4
# print((9 + 7) % 12)


stacys_mom = "got it goin on"
waited = "for so long"
print(f"stacey's mom has",stacys_mom,"she's all I want and I've",waited,)

