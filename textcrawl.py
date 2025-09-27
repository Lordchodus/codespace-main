import random

# room list, contents dictionary, and notes dictionary
room_list = []      # List for rooms
room_contents = {}  # Dictionary for Contents
room_notes = {}     # Dictionary for user notes
search_results = {} # Dictionary for search results

# combat
spell_roll = random.randint(1, 6)

#  Instructions
print("Room Generator & Dice Roller for Four Against Darkness\n")
print("Roll Rooms, Generate Contents, Add Notes, and Roll Dice\n")
print("Commands: 'room/r' 'dice/d' 'list/l' 'notes/n' 'search/s' 'contents/c' 'help/h/?' 'quit/q/exit'")

# main loop
while True: # Loop until user quits
    user_input = input("\nEnter Command: ").lower().strip()
    
    if user_input in ['quit', 'q', 'exit']:
        break
    elif user_input in ['help', 'h', '?']:
        print("Type 'room' or 'r' to generate a room.\n")
        print("Type 'contents' to generate contents for the current room.\n")
        print("Type 'search' to search the current room if it is searchable.\n")
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
                content = "Empty, Can Search"
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
                content = "Empty, Can Search"
            elif d6_total == 5 and current_room_type == "Corridor":
                content = "Roll d6 Special Features Table"
            elif d6_total == 6 and current_room_type == "Corridor":
                content = "Roll d6 Vermin Table"
            elif d6_total == 7 and current_room_type == "Corridor":
                content = "Roll d6 Minions Table"
            elif d6_total == 8 and current_room_type == "Corridor":
                content = "Empty, Can Search"
            elif d6_total == 9 and current_room_type == "Corridor":
                content = "Empty, Can Search"
            elif d6_total == 10 and current_room_type == "Corridor":
                content = "Empty, Can Search"
            elif d6_total == 11 and current_room_type == "Corridor":
                content = "Roll d6 Boss Table"
            elif d6_total == 12 and current_room_type == "Corridor":
                content = "Empty, Can Search"
            
            
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
                contents = room_contents.get(index, 'No contents generated, press c to generate contents')
                notes = room_notes.get(index, 'No notes')
                print(f"{room} # {index}.")
                print(f"   Contents: {contents}")
                print(f"   Notes: {notes}")
                print(f"   Search Status: {'Searched' if index in search_results else 'Not Searched'}")
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
            print("Generate a room first")  
        if not room_contents:
            print("Generate room contents first")
            continue
        if "Empty, Can Search" not in room_contents.values():
            print("Can't Search")
            continue

        current_room_num = len(room_list)
        current_contents = room_contents.get(current_room_num)

        if current_room_num in search_results:
            print(f"You already searched this room")
            continue
        d6_roll = random.randint(1, 6)
        print(f"\nd6: {d6_roll}\n")
        if d6_roll == 1:
            print(f"\nRoll on the wandering monster table\n")  
        if d6_roll == 1:
            wmd6_roll = random.randint(1, 6)
            print(f"\nd6: {wmd6_roll}\n")
            if wmd6_roll == 1 or wmd6_roll == 2:
                    print(f"\nRoll on vermin table\n")
                    vermin_roll = random.randint(1, 6)
                    print(f"\nd6: {vermin_roll}\n")
                    if vermin_roll == 1:
                        rats = random.randint(3, 18)
                        rat_lvl = 1
                        rat_ability = spell_roll - 1
                        print(f"\nyou are attacked by {rats} rats!\n")
                        print(f"Rats are level {rat_lvl} with ability when wounded 1d6 additional life lost\n")
                    elif vermin_roll == 2:
                        bats = random.randint(3, 18)
                        print(f"\nyou are attacked by {bats} bats!\n")
                    elif vermin_roll == 3:
                        goblin_swarmlings = random.randint(2, 12)
                        print(f"\nyou are attacked by {goblin_swarmlings} goblin swarmlings!\n")
                    elif vermin_roll == 4:
                        giant_centipedes = random.randint(1, 6)
                        print(f"\n you are attacked by {giant_centipedes} giant centipedes!\n")
                    elif vermin_roll == 5:
                        vampire_frogs = random.randint(1, 6)
                        print(f"you are attacked by {vampire_frogs} vampire frogs!\n")
                    elif vermin_roll == 6:
                        skeletal_rats = random.randint(2, 12)
                        print(f"you are attacked by {skeletal_rats} skeletal rats!")
            elif wmd6_roll == 3 or wmd6_roll == 4:
                    print(f"\nRoll on minions table\n")
                    minion_roll = random.randint(1, 6)
                    print(f"\nd6: {minion_roll}\n")
                    if minion_roll == 1:
                        minion1_roll = random.randint(1, 6)
                        print(f"\nd6: {minion1_roll}\n")
                        if minion1_roll <= 3:
                            skeletons = random.randint(1, 6) + 2
                            print(f"\nyou are attacked by {skeletons} skeletons!\n")
                        elif minion1_roll >= 4:
                            zombies = random.randint(1, 6)
                            print(f"\nyou are attacked by {zombies} zombies!\n")
            elif wmd6_roll == 5:
                    print(f"\nRoll on weird monster table\n")
            elif wmd6_roll == 6:
                    print(f"\nRoll on boss table\n")
        elif d6_roll == 2 or d6_roll == 3 or d6_roll == 4:
                print(f"\nCound't Find Anything..\n")
        elif d6_roll == 5 or d6_roll == 6:
                print(f"\nChoose: you found a clue, a secret door, or a hidden treasure!\n")
        search_results[current_room_num] = "Searched"
            
    else:
        print("Unknown command. Try 'room/r', 'dice/d', 'list/l', 'contents/c', 'search/s' 'notes/n' or 'quit/q/exit'.")

print("Goodbye!")