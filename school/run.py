import random

def d6_roll():
    return random.randint(1, 6)

def d8_roll():
    return random.randint(1, 8)

def d10_roll():
    return random.randint(1, 10)

while True: 
    command = input("Enter command: ").lower().strip()
 
    if command in ['d6']:
        result = d6_roll()  # Call once and store the result
        print(f"you rolled a {result}")
    elif command in ['d8']:
        result = d8_roll()
        print(f"you rolled a {result}")
    elif command in ['d10']:
        result = d10_roll()
        print(f"you rolled a {result}")    

    
