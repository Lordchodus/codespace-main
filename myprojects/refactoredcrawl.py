import random

# ---------------------------
# Constants
# ---------------------------
SEARCHABLE = "Empty, Can Search"

# ---------------------------
# Lookup tables
# ---------------------------
room_results = {
    2: "Roll d6 Treasure Table",
    3: "Roll d6 Traps Table",
    4: "Roll d6 Special Events Table",
    5: "Roll d6 Special Features Table",
    6: "Roll d6 Vermin Table",
    7: "Roll d6 Minions Table",
    8: "Roll d6 Minions Table",
    9: SEARCHABLE,
    10: "Roll d6 Weird Monsters Table",
    11: "Roll d6 Boss Table + 6 on d6 = Final Boss",
    12: "Dragon Lair",
}

corridor_results = {
    2: "Roll d6 Treasure Table",
    3: "Roll d6 Traps Table",
    4: SEARCHABLE,
    5: "Roll d6 Special Features Table",
    6: "Roll d6 Vermin Table",
    7: "Roll d6 Minions Table",
    8: SEARCHABLE,
    9: SEARCHABLE,
    10: SEARCHABLE,
    11: "Roll d6 Boss Table",
    12: SEARCHABLE,
}

# ---------------------------
# Game data
# ---------------------------
room_list = []
room_contents = {}
room_notes = {}
search_results = {}

# ---------------------------
# Helper functions
# ---------------------------
def roll(sides, num=1):
    """Roll dice and return a list of results."""
    return [random.randint(1, sides) for _ in range(num)]

def get_room_content(room_type, total):
    """Return contents for a room or corridor given 2d6 total."""
    if room_type == "Room":
        return room_results[total]
    else:
        return corridor_results[total]

def wandering_monster():
    """Pick a wandering monster encounter."""
    roll_val = random.randint(1, 6)
    if roll_val <= 2:
        return "Roll on vermin table"
    elif roll_val <= 4:
        return "Roll on minions table"
    elif roll_val == 5:
        return "Roll on weird monster table"
    else:
        return "Roll on boss table"

def list_rooms():
    """Display all generated rooms, contents, notes, and search status."""
    if not room_list:
        print("No rooms generated yet.")
        return
    print("\nGenerated Rooms:")
    for index, room in enumerate(room_list, 1):
        contents = room_contents.get(index, 'No contents generated')
        notes = room_notes.get(index, 'No notes')
        searched = "Searched" if index in search_results else "Not Searched"
        print(f"{room} #{index}:")
        print(f"   Contents: {contents}")
        print(f"   Notes: {notes}")
        print(f"   Search Status: {searched}")
        print()

# ---------------------------
# Main Loop
# ---------------------------
print("Room Generator & Dice Roller for Four Against Darkness\n")
print("Commands: 'room/r' 'dice/d' 'list/l' 'notes/n' 'search/s' 'contents/c' 'help/h/?' 'quit/q/exit'")

while True:
    user_input = input("\nEnter Command: ").lower().strip()

    # ---- quit ----
    if user_input in ['quit', 'q', 'exit']:
        break

    # ---- help ----
    elif user_input in ['help', 'h', '?']:
        print("Type 'room' or 'r' to generate a room.")
        print("Type 'contents' to generate contents for the current room.")
        print("Type 'search' to search the current room if it is searchable.")
        print("Type 'dice' to roll dice.")
        print("Type 'notes' to add notes to the current room.")
        print("Type 'list' to see all rooms, contents, and notes.")
        print("Type 'quit' to exit.")

    # ---- generate room ----
    elif user_input in ['room', 'r']:
        room_type = "Room" if random.randint(1, 3) != 2 else "Corridor"
        room_list.append(room_type)
        print(f"Rolled a {room_type}")

    # ---- generate contents ----
    elif user_input in ['contents', 'c']:
        if not room_list:
            print("Generate a room first.")
            continue

        current_room_num = len(room_list)
        if current_room_num in room_contents:
            print(f"Contents already exist for Room {current_room_num}: {room_contents[current_room_num]}")
            continue

        room_type = room_list[-1]
        d6_total = sum(roll(6, 2))
        print(f"2d6 rolled: {d6_total}")

        content = get_room_content(room_type, d6_total)
        room_contents[current_room_num] = content
        print(f"Room {current_room_num}: {room_type} - {content}")

    # ---- dice roller ----
    elif user_input in ['dice', 'd']:
        print(f"d6: {roll(6)[0]}")
        d6s = roll(6, 2)
        print(f"2d6: {d6s[0]} + {d6s[1]} = {sum(d6s)}")
        print(f"d4: {roll(4)[0]}")
        print(f"d20: {roll(20)[0]}")
        print(f"d66: {random.randint(11, 66)}")

    # ---- list rooms ----
    elif user_input in ['list', 'l']:
        list_rooms()

    # ---- notes ----
    elif user_input in ['notes', 'n']:
        if not room_list:
            print("No rooms yet.")
            continue
        current_room_num = len(room_list)
        print(f"Adding note for Room {current_room_num} ({room_list[-1]}).")
        if current_room_num in room_contents:
            print(f"Contents: {room_contents[current_room_num]}")
        note_text = input("Enter note: ").strip()
        room_notes[current_room_num] = note_text
        print("Note saved.")

    # ---- search ----
    elif user_input in ['search', 's']:
        if not room_list:
            print("Generate a room first.")
            continue

        current_room_num = len(room_list)
        contents = room_contents.get(current_room_num)

        if not contents:
            print("Generate room contents first.")
            continue
        if contents != SEARCHABLE:
            print(f"Room {current_room_num} cannot be searched (contents = {contents})")
            continue
        if current_room_num in search_results:
            print("Already searched this room.")
            continue

        d6_result = roll(6)[0]
        print(f"d6 rolled: {d6_result}")

        if d6_result <= 6:  # wandering monster case
            print(wandering_monster())
        # you can expand this with your specific monster tables

        search_results[current_room_num] = "Searched"

    # ---- unknown ----
    else:
        print("Unknown command. Try 'help' for a list of commands.")

print("Goodbye!")
