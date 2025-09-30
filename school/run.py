import random

rolls = {
    'd6': lambda: random.randint(1, 6),
    'd8': lambda: random.randint(1, 8),
    'd10': lambda: random.randint(1, 10),
    'd12': lambda: random.randint(1, 12),
    'd20': lambda: random.randint(1, 20),
}


while True: 
    command = input("Enter command: ").lower().strip()
    if command in ['quit']:
        break
    elif command in ['d6']:
        result = rolls['d6']()  # Call once and store the result
        print(f"you rolled a {result}")
    elif command in ['d8']:
        result = rolls['d8']()
        print(f"you rolled a {result}")
    elif command in ['d10']:
        result = rolls['d10']()
        print(f"you rolled a {result}")
    

