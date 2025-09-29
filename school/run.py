# 1. Plan functions: make a bullet list of the actions and helpers you’ll need.
# 2. write the pantry dictionary and your first function (like add_snack).
# 3. Build out actions: add remove and list features, with careful error checks.
# 4. Add input validation: make sure users can’t add “-5 Oreos” or “ ” as a snack.
# 5. Testing: write at least 3 small tests for your helpers.
# 6. Polish: run through a main loop for user interaction, then clean up prints.

pantry = {}

print("Pantry Tracker\n")
print("add, remove, and list items in pantry")
print("commands: 'add' 'remove' and 'list' 'help' 'quit'")

while True:
    pantry_track = input("Enter Command: ").lower().strip()

    if pantry_track in ['quit']:
        break
    elif pantry_track in ['help']:
        print("Type 'add' to add items to pantry")
        print("Type 'remove' to remove from pantry")
        print("Type 'list to list items in pantry")
        print("Type 'quit to exit the program")

    elif pantry_track in ['add']:
        print("Enter item: ")
        print("")
