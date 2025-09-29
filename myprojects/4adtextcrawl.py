import random

# room list, contents dictionary, and notes dictionary
room_list = []      # List for rooms
room_contents = {}  # Dictionary for Contents
room_notes = {}     # Dictionary for user notes

#  Instructions
print("Room Generator & Dice Roller for Four Against Darkness\n")
print("Roll Rooms, Generate Contents, Add Notes, and Roll Dice\n")
print("Commands: 'room' 'dice' 'list' 'notes' 'contents' 'help' 'quit")

# main loop
while True: # Loop until user quits
    user_input = input("\nEnter Command: ").lower().strip()
    
    if user_input in ['quit', 'q', 'exit']:
        break
    elif user_input in ['help', 'h', '?']:
        print("Type 'room' or 'r' to generate a room.\n")
        print("Type 'contents' to generate contents for the current room.\n")
        print("Type 'dice' to roll dice.\n")
        print("Type 'notes' to add notes to the current room.\n")
        print("Type 'list' to see all generated rooms, their contents and notes.\n")
        print("Type 'quit' to exit.\n")

    elif user_input in ['room', 'r']:
        gen_rooms = random.randint(1, 3) # 1 = Room, 2 = Corridor, 3 = Room
        if gen_rooms == 1:
            room_type = "Room"
        elif gen_rooms == 2:
            room_type = "Corridor"
        else:
            room_type = "Room"
        
        room_list.append(room_type) # Add room to list
        print(f"Rolled a {room_type}\n")
    
    elif user_input in ['contents', 'c']:
        if not room_list:
            print("Generate a room first")
            
        else:
            current_room_num = len(room_list)
            if current_room_num in room_contents: # check room number in contents if found no more contents can be created
                print(f"Contents already generated for Room {current_room_num}: {room_contents[current_room_num]}")
                continue
            current_room_type = room_list[-1] # Last room in list
            content = "" # Initialize content variable
            d6_roll1 = random.randint(1, 6)
            d6_roll2 = random.randint(1, 6)
            d6_total = d6_roll1 + d6_roll2
            print(f"2d6: {d6_roll1} + {d6_roll2} = {d6_total}")
            
            if d6_total == 2 and current_room_type == "Room":
                content = "Roll d6 Treasure Table"
            elif d6_total == 3 and current_room_type == "Room":
                content = "Roll d6 Traps Table"
            elif d6_total == 4 and current_room_type == "Room":
                content = "Roll d6 Special Events Table"
            elif d6_total == 5 and current_room_type == "Room":
                content = "Roll d6 Special Features Table"
            elif d6_total == 6 and current_room_type == "Room":
                content = "Roll d6 Vermin Table"
            elif d6_total == 7 and current_room_type == "Room":
                content = "Roll d6 Minions Table"
            elif d6_total == 8 and current_room_type == "Room":
                content = "roll d6 Minions Table"
            elif d6_total == 9 and current_room_type == "Room":
                content = "Room Empty, Can Search"
            elif d6_total == 10 and current_room_type == "Room":
                content = "Roll d6 Weird Monsters Table"
            elif d6_total == 11 and current_room_type == "Room":
                content = "Roll d6 Boss Table + 6 on d6 = Final Boss"
            elif d6_total == 12 and current_room_type == "Room":
                content = "Dragon Lair"
            elif d6_total == 2 and current_room_type == "Corridor":
                content = "Roll d6 Treasure Table"
            elif d6_total == 3 and current_room_type == "Corridor":
                content = "Roll d6 Traps Table"
            elif d6_total == 4 and current_room_type == "Corridor":
                content = "Room Empty, Can Search"
            elif d6_total == 5 and current_room_type == "Corridor":
                content = "Roll d6 Special Features Table"
            elif d6_total == 6 and current_room_type == "Corridor":
                content = "Roll d6 Vermin Table"
            elif d6_total == 7 and current_room_type == "Corridor":
                content = "Roll d6 Minions Table"
            elif d6_total == 8 and current_room_type == "Corridor":
                content = "Corridor Empty, Can Search"
            elif d6_total == 9 and current_room_type == "Corridor":
                content = "Corridor Empty, Can Search"
            elif d6_total == 10 and current_room_type == "Corridor":
                content = "Corridor Empty, Can Search"
            elif d6_total == 11 and current_room_type == "Corridor":
                content = "Roll d6 Boss Table"
            elif d6_total == 12 and current_room_type == "Corridor":
                content = "Corridor Empty, Can Search"
            
            
            room_contents[current_room_num] = content # Save content in separate dictionary
            print(f"Room {current_room_num}: {current_room_type} - {content}\n")

    elif user_input in ['dice', 'd']:
        d6_roll = random.randint(1, 6)
        print(f"\nd6: {d6_roll}\n")

        d6_roll1 = random.randint(1, 6)
        d6_roll2 = random.randint(1, 6)
        d6_total = d6_roll1 + d6_roll2
        print(f"\n2d6: {d6_roll1} + {d6_roll2} = {d6_total}\n")
        
        d4_roll = random.randint(1, 4)
        print(f"\nd4: {d4_roll}\n")
        
        d20_roll = random.randint(1, 20)
        print(f"\nd20: {d20_roll}\n")
        
        d66_roll = random.randint(11, 66)
        print(f"\nd66: {d66_roll}\n")
    
    elif user_input in ['list', 'l']:
        if room_list:
            print("\nGenerated Rooms:")
            for index, room in enumerate(room_list, 1):
                contents = room_contents.get(index, 'No contents generated')
                notes = room_notes.get(index, 'No notes')
                print(f"{index}. {room}")
                print(f"   Contents: {contents}")
                print(f"   Notes: {notes}")
                print()
        else:
            print("No rooms generated yet.")
    elif user_input in ['notes','n']:
        if not room_list:
            print("No rooms to add notes to. Generate a room first.")
        else:
            current_room_num = len(room_list)  # Most recent room
            current_room_type = room_list[-1]  # Last room in list
            print(f"Adding note for Room {current_room_num}: {current_room_type}")
            
            # Show existing content if any
            if current_room_num in room_contents:
                print(f"Current contents: {room_contents[current_room_num]}")
            
            note_text = input("Enter room note: ").strip()
            room_notes[current_room_num] = note_text
            print(f"Note saved: {note_text}")
    
    elif user_input in ['search','s']:
        if not room_list:
            print("No rooms generated. Generate a room first.")
    else:
        current_room_num = len(room_list)
        
        # Check if current room has contents generated
        if current_room_num not in room_contents:
            print("Generate contents for this room first before searching.")
        else:
            room_content = room_contents[current_room_num]
            
            # Check if the room can be searched
            if "Can Search" in room_content:
                d6_roll = random.randint(1, 6)
                print(f"\nSearch roll d6: {d6_roll}\n")
                if d6_roll <= 6:  # Note: this condition will always be true, you might want to adjust
                    sd6_roll = random.randint(1, 6)
                    print(f"Roll on the wandering monster table: {sd6_roll}\n")
                    if sd6_roll == 1 or sd6_roll == 2:
                        print("Roll on vermin table")
                    elif sd6_roll == 3 or sd6_roll == 4:
                        print("Roll on minions table")
                    elif sd6_roll == 5:
                        print("Roll on weird monsters table")
                    elif sd6_roll == 6:
                        print("Roll on boss table")
            else:
                print(f"Cannot search this room. Current contents: {room_content}")
                print("Only rooms/corridors that are empty and can be searched allow searching.")
        

print("Goodbye!")