import random

def d6_roll():
    return random.randint(1, 6)

while True: 
    command = input("Enter command: ").lower().strip()
    print(f"debug: you typed '{command}'")
 
    if command in ['roll']:
        result = d6_roll()  # Call once and store the result
        print(f"you rolled a {result}")
    

    
