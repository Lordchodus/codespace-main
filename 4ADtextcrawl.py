import random

# room list and notes dictionary
room_list = []
room_notes = {}

#  Instructons
print("Room Generator & Dice Roller")
print("Type 'room' to generate a room.")
print("Type 'dice' to roll dice.")
print("Type 'notes' to add notes to the most recent room.")
print("Type 'list' to see all generated rooms and their notes.")
print("Type 'quit' to exit.")
print("Commands: 'room', 'dice', 'list', 'notes','contents' 'quit'")

# main loop
while True:
    user_input = input("\nEnter Command: ").lower().strip()
    
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
        print(f"Rolled a {room_type}")
    
    elif user_input == 'contents':
        if not room_list:
            print("No rooms to add contents to. Generate a room first!")
        else:
            current_room_num = len(room_list)
            current_room_type = room_list[-1]
            d6_roll1 = random.randint(1, 6)
            d6_roll2 = random.randint(1, 6)
            d6_total = d6_roll1 + d6_roll2
            print(f"2d6: {d6_roll1} + {d6_roll2} = {d6_total}")
            if d6_total == 2 and current_room_type == "Room":
                print("Roll d6 Treasure Table")
            elif d6_total == 3 and current_room_type == "Room":
                print("Roll d6 Traps Table")
            elif d6_total == 4 and current_room_type == "Room":
                print("Roll d6 Special Events Table")
            elif d6_total == 5 and current_room_type == "Room":
                print("Roll d6 Special Features Table")
            elif d6_total == 6 and current_room_type == "Room":
                print("Roll d6 Vermin Table")
            elif d6_total == 7 and current_room_type == "Room":
                print("Roll d6 Minions Table")
            elif d6_total == 8 and current_room_type == "Room":
                print("roll d6 Minions Table")
            elif d6_total == 9 and current_room_type == "Room":
                print("Room Empty, Can Search")
            elif d6_total == 10 and current_room_type == "Room":
                print("Roll d6 Weird Monsters Table")
            elif d6_total == 11 and current_room_type == "Room":
                print("Roll d6 Boss Table + 6 on d6 = Final Boss")
            elif d6_total == 12 and current_room_type == "Room":
                print("Dragon Lair")
            elif d6_total == 2 and current_room_type == "Corridor":
                print("Roll d6 Treasure Table")
            elif d6_total == 3 and current_room_type == "Corridor":
                print("Roll d6 Traps Table")
            elif d6_total == 4 and current_room_type == "Corridor":
                print("Room Empty, Can Search")
            elif d6_total == 5 and current_room_type == "Corridor":
                print("Roll d6 Special Features Table")
            elif d6_total == 6 and current_room_type == "Corridor":
                print("Roll d6 Vermin Table")
            elif d6_total == 7 and current_room_type == "Corridor":
                print("Roll d6 Minions Table")
            elif d6_total == 8 and current_room_type == "Corridor":
                print("Corridor Empty, Can Search")
            elif d6_total == 9 and current_room_type == "Corridor":
                print("Corridor Empty, Can Search")
            elif d6_total == 10 and current_room_type == "Corridor":
                print("Corridor Empty, Can Search")
            elif d6_total == 11 and current_room_type == "Corridor":
                print("Roll d6 Boss Table")
            elif d6_total == 12 and current_room_type == "Corridor":
                print("Corridor Empty, Can Search")


    elif user_input == 'dice':
        d6_roll = random.randint(1, 6)
        print(f"d6: {d6_roll}")

        d6_roll1 = random.randint(1, 6)
        d6_roll2 = random.randint(1, 6)
        d6_total = d6_roll1 + d6_roll2
        print(f"2d6: {d6_roll1} + {d6_roll2} = {d6_total}")
        
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
                print(f"{index}. {room} - {room_notes.get(index, 'No notes')}")
        else:
            print("No rooms generated yet.")
    elif user_input == 'notes':
        if not room_list:
            print("No rooms to add notes to. Generate a room first!")
        else:
            current_room_num = len(room_list)  # Most recent room
            current_room_type = room_list[-1]  # Last room in list
            print(f"Adding note for the current room (Room {current_room_num}: {current_room_type})")
            note_text = input("Enter your note: ")
            room_notes[current_room_num] = note_text
            print(f"Note saved: {note_text}")
    else:
        print("Unknown command. Try 'room', 'dice', 'list', or 'quit'")

print("Goodbye!")