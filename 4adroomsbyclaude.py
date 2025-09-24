import random

# Initialize the list outside the loop so it persists
room_list = []

print("Room Generator & Dice Roller")
print("Commands: 'room', 'dice', 'list', 'quit'")

while True:
    user_input = input("\nWhat would you like to do? ").lower().strip()
    
    if user_input == 'quit':
        break
    
    elif user_input == 'room':
        gen_rooms = random.randint(1, 3)
        if gen_rooms == 1:
            room_type = "Room"
        elif gen_rooms == 2:
            room_type = "Corridor"
        else:
            room_type = "Room"
        
        room_list.append(room_type)
        print(f"Generated a {room_type}")
    
    elif user_input == 'dice':
        d6_roll = random.randint(1, 6)
        print(f"d6: {d6_roll}")
        
        d4_roll = random.randint(1, 4)
        print(f"d4: {d4_roll}")
        
        d20_roll = random.randint(1, 20)
        print(f"d20: {d20_roll}")
        
        d66_roll = random.randint(11, 66)
        print(f"d66: {d66_roll}")
    
    elif user_input == 'list':
        if room_list:
            print("\nGenerated rooms:")
            for index, room in enumerate(room_list, 1):
                print(f"{index}. {room}")
        else:
            print("No rooms generated yet.")
    
    else:
        print("Unknown command. Try 'room', 'dice', 'list', or 'quit'")

print("Goodbye!")