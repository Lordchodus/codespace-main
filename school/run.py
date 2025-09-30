# 1. Plan functions: make a bullet list of the actions and helpers you’ll need.
# 2. write the pantry dictionary and your first function (like add_snack).
# 3. Build out actions: add remove and list features, with careful error checks.
# 4. Add input validation: make sure users can’t add “-5 Oreos” or “ ” as a snack.
# 5. Testing: write at least 3 small tests for your helpers.
# 6. Polish: run through a main loop for user interaction, then clean up prints.

pantry = {}
current_command = None  # keeps track of what we’re doing

print("Pantry Tracker\n")
print("add, remove, and list items in pantry")
print("commands: 'add' 'remove' 'list' 'help' 'quit'")

while True:
    pantry_track = input("Enter Command or Item: ").lower().strip()

    # --- quit ---
    if pantry_track == 'quit':
        break

    # --- help ---
    elif pantry_track == 'help':
        print("Type 'add' to add items to pantry")
        print("Type 'remove' to remove from pantry")
        print("Type 'list' to list items in pantry")
        print("Type 'quit' to exit the program")
        current_command = None

    # --- list ---
    elif pantry_track == 'list':
        if pantry:
            for item, qty in pantry.items():
                print(f"{item}: x{qty}")
        else:
            print("Pantry is empty.")
        current_command = None

    # --- add mode ---
    elif pantry_track == 'add':
        print("type an item name (or any command to switch: 'add', 'remove', 'list', 'quit').")
        current_command = 'add'

    elif current_command == 'add':
        # If they typed another command, switch out of add mode
        if pantry_track in ['remove', 'list', 'help', 'quit', 'add']:
            current_command = None  # reset so next loop treats it as command
            pantry_track = pantry_track  # treat as new command
            # re-run this loop iteration by pretending they typed the command
            continue

        # otherwise, treat input as item
        item = pantry_track
        quantity = int(input("Enter quantity: "))

        if item in pantry:
            pantry[item] += quantity
        else:
            pantry[item] = quantity

        print(f"Added {quantity} {item}. Now you have {pantry[item]} in the pantry.")

    # --- remove (you can expand later) ---
    elif pantry_track == 'remove':
        if pantry_track in ['add', 'list', 'help', 'remove', 'quit']:
            current_command = None
            pantry_track = pantry_track
            continue
        item = pantry_track
        quantity = int(input("how many to remove?: "))
        if item in pantry:
            pantry[item] -= quantity
        else:
            pantry[item] = quantity
        print(f" removed {quantity} {item} from pantry. {pantry[item]} in pantry")

    else:
        print("Unknown command. Type 'help' for options.")

    
