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
    
    if command == 'quit':
        break
    elif command in rolls:  # Check if it's a valid dice command
        result = rolls[command]()
        print(f"You rolled a {result}")
    else:
        print("Unknown command. Try: d6, d8, d10, d12, d20, or quit")
    

