import random

# VALUE STORAGE
room_list = []
room_contents = {}
room_notes = {}
search_results = {}
current_room_index = 0

# DICE ROLLER
def roll(sides):
    return random.randint(1, sides)

# ROOM CONTENT TABLES

ROOM_CONTENTS = {
    
    "Room": 
    {
        2: "Roll d6 Treasure Table",
        3: "Roll d6 Traps Table",
        4: "Roll d6 Special Events Table",
        5: "Roll d6 Special Features Table",
        6: "Roll d6 Vermin Table",
        7: "Roll d6 Minions Table",
        8: "roll d6 Minions Table",
        9: "Empty, Can Search",
        10: "Roll d6 Weird Monsters Table",
        11: "Roll d6 Boss Table + 6 on d6 = Final Boss",
        12: "Dragon Lair"
    },
    
    "Corridor": 
    {
        2: "Roll d6 Treasure Table",
        3: "Roll d6 Traps Table",
        4: "Empty, Can Search",
        5: "Roll d6 Special Features Table",
        6: "Roll d6 Vermin Table",
        7: "Roll d6 Minions Table",
        8: "Empty, Can Search",
        9: "Empty, Can Search",
        10: "Empty, Can Search",
        11: "Roll d6 Boss Table",
        12: "Empty, Can Search"
    }
}

# VERMIN ENCOUNTER TABLE
VERMIN_TABLE = {
    1: lambda: (roll(6) + roll(6) + roll(6), 
                "rats", 1, "when attack hits, " 
                "defender loses 1 additional life"),
    2: lambda: (roll(6) + roll(6) + roll(6), "bats", 1, ""),
    3: lambda: (roll(6) + roll(6), "goblin swarmlings", 1, ""),
    4: lambda: (roll(6), "giant centipedes", 2, ""),
    5: lambda: (roll(6), "vampire frogs", 2, ""),
    6: lambda: (roll(6) + roll(6), "skeletal rats", 1, "")
}

# MINION ENCOUNTER TABLE
#MINION_TABLE = {
#    1: lambda: (roll(6))
#}

# COMMAND FUNCTIONS
def generate_room():
    room_type = "Corridor" if roll(3) == 2 else "Room"
    room_list.append(room_type)
    print(f"Rolled a {room_type}\n")

def generate_contents():
    if not room_list:
        print("Generate a room first")
        return
    
    current_room_num = len(room_list)
    
    if current_room_num in room_contents:
        print(f"Contents already generated for Room {current_room_num}: {room_contents[current_room_num]}")
        return
    
    current_room_type = room_list[-1]
    d6_roll1 = roll(6)
    d6_roll2 = roll(6)
    d6_total = d6_roll1 + d6_roll2
    print(f"2d6: {d6_roll1} + {d6_roll2} = {d6_total}")
    
    content = ROOM_CONTENTS[current_room_type].get(d6_total, "Unknown")
    room_contents[current_room_num] = content
    print(f"Room {current_room_num}: {current_room_type} - {content}\n")

def roll_dice():
    print(f"\nd6: {roll(6)}\n")
    d6_1, d6_2 = roll(6), roll(6)
    print(f"2d6: {d6_1} + {d6_2} = {d6_1 + d6_2}\n")
    print(f"d4: {roll(4)}\n")
    print(f"d20: {roll(20)}\n")
    print(f"d66: {roll(56) + 10}\n")  

def list_rooms():
    if not room_list:
        print("No rooms generated yet.")
        return
    
    print("\nGenerated Rooms:")
    for index, room in enumerate(room_list, 1):
        contents = room_contents.get(index, 'No contents generated, press c to generate contents')
        notes = room_notes.get(index, 'No notes')
        search_result = search_results.get(index, 'Not searched')
        
        print(f"#{index} {room}.")
        print(f"   Contents: {contents}")
        print(f"   Notes: {notes}")
        print(f"   Search: {search_result}")
        print()

def add_notes():
    if not room_list:
        print("No rooms to add notes to. Generate a room first.")
        return
    
    current_room_num = len(room_list)
    current_room_type = room_list[-1]
    
    print(f"Adding note for Room {current_room_num}: {current_room_type}")
    
    if current_room_num in room_contents:
        print(f"Current contents: {room_contents[current_room_num]}")
    
    note_text = input("Enter room note: ").strip()
    room_notes[current_room_num] = note_text
    print(f"Note saved: {note_text}")

def vermin_encounter(vermin_roll):
    count, name, level, ability = VERMIN_TABLE[vermin_roll]()
    print(f"\nYou are attacked by {count} {name}!\n")
    if ability:
        print(f"{name.capitalize()} are level {level} with ability: {ability}\n")
    return count, name
    

def minion_encounter():
    minion_roll = roll(6)
    print(f"\nd6: {minion_roll}\n")
    
    if minion_roll == 1:
        minion1_roll = roll(6)
        print(f"\nd6: {minion1_roll}\n")
        if minion1_roll <= 3:
            skeletons = roll(6) + 2
            print(f"\nYou are attacked by {skeletons} skeletons!\n")
        else:
            zombies = roll(6)
            print(f"\nYou are attacked by {zombies} zombies!\n")

def search_room():
    if not room_list:
        print("Generate a room first")
        return
    
    current_room_num = len(room_list)
    current_contents = room_contents.get(current_room_num)
    
    if not current_contents:
        print("Generate room contents first")
        return
    if current_contents != "Empty, Can Search":
        print(f"Room {current_room_num} can't be searched")
        return
    if current_room_num in search_results:
        print("You already searched this room")
        return
    
    # SEARCH ROLL
    search_roll = roll(6)
    print(f"\nd6: {search_roll}\n")
    
    if search_roll == 1:
        print("\nRoll on the wandering monster table\n")
        wandering_monsters_roll = roll(6)
        print(f"\nd6: {wandering_monsters_roll}\n")
        
        if wandering_monsters_roll in [1, 2]:
            print("\nRoll on vermin table\n")
            vermin_roll = roll(6)
            print(f"\nd6: {vermin_roll}\n")
            vermin_encounter(vermin_roll)
            count, name = vermin_encounter(vermin_roll)
            search_results[current_room_num] = "Wandering Monster: Vermin {count} {name}"
        elif wandering_monsters_roll in [3, 4]:
            print("\nRoll on minions table\n")
            minion_encounter()
            search_results[current_room_num] = "Wandering Monster: Minion"
        elif wandering_monsters_roll == 5:
            print("\nRoll on weird monster table\n")
            search_results[current_room_num] = "Wandering Monster: Weird"
        elif wandering_monsters_roll == 6:
            print("\nRoll on boss table\n")
            search_results[current_room_num] = "Wandering Monster: Boss"
    
    elif search_roll in [2, 3, 4]:
        print("\nCouldn't find anything..\n")
        search_results[current_room_num] = "Nothing Found"
    
    elif search_roll in [5, 6]:
        print("\nChoose: you found a clue, a secret door, or a hidden treasure!\n")
        choice = input("Type 'clue/c', 'door/d', or 'treasure/t': ").lower().strip()
        
        if choice in ['clue', 'c']:
            print("You found a clue")
            search_results[current_room_num] = "found: clue"
        elif choice in ['door', 'd']:
            print("You found a secret door")
            search_results[current_room_num] = "found: secret door"
        elif choice in ['treasure', 't']:
            search_results[current_room_num] = "found: hidden treasure"
            print("You found a secret treasure")

def show_help():
    print("Type 'room' or 'r' to generate a room.\n")
    print("Type 'contents' to generate contents for the current room.\n")
    print("Type 'search' to search the current room if it is searchable.\n")
    print("Type 'dice' to roll dice.\n")
    print("Type 'notes' to add notes to the current room.\n")
    print("Type 'list' to see all generated rooms, their contents and notes.\n")
    print("Type 'quit' to exit.\n")

# COMMAND MAPPING
COMMANDS = {
    'room': generate_room,
    'r': generate_room,
    'contents': generate_contents,
    'c': generate_contents,
    'dice': roll_dice,
    'd': roll_dice,
    'list': list_rooms,
    'l': list_rooms,
    'notes': add_notes,
    'n': add_notes,
    'search': search_room,
    's': search_room,
    'help': show_help,
    'h': show_help,
    '?': show_help
}

# MAIN PROGRAM
def main():
    print("Room Generator & Dice Roller for Four Against Darkness\n")
    print("Roll Rooms, Generate Contents, Add Notes, and Roll Dice\n")
    print("Commands: 'room/r' 'dice/d' 'list/l' 'notes/n' 'search/s' 'contents/c' 'help/h/?' 'quit/q/exit'")
    
    while True:
        user_input = input("\nEnter Command: ").lower().strip()
        
        if user_input in ['quit', 'q', 'exit']:
            break
        elif user_input in COMMANDS:
            COMMANDS[user_input]()
        else:
            print(
                
                "Unknown command. Try 'room/r', 'dice/d', " \
                "'list/l', 'contents/c', 'search/s', 'notes/n', "
                "or 'quit/q/exit'."
                
                )
    
    print("Goodbye!")

main()