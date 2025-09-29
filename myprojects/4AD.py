import random
room_list = []
gen_rooms = random.randint(1, 3)
if gen_rooms == 1:
    room_type = "Room"
elif gen_rooms == 2:
    room_type = "Corridor"
else:
    room_type = "Room"
room_list.append(room_type)
print(f"Generated a {room_type}")

print("\nGenerated rooms:")
for index, room in enumerate(room_list, 1):  # Start counting from 1
    print(f"{index}. {room}")


d6_roll = random.randint(1, 6)
print(f"You rolled a {d6_roll}")

d4_roll = random.randint(1, 4)
print(f"You rolled a {d4_roll}")

d20_roll = random.randint(1, 20)
print(f"You rolled a {d20_roll}")

d66_roll = random.randint(11, 66)
print(f"You rolled a {d66_roll}")
# 4AD.py

# 14 corridors
# 