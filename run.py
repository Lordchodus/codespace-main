

fav_food = ["pizza", "sushi", "tacos"]
for i, food in enumerate(fav_food):
    print(f"{i+1}. {food}")

for i, food in enumerate(fav_food, 1):
    print(f"{i}. {food}")


pets = ["dog", "cat"]
gone = pets.pop(0)
for i, pets in enumerate(pets, 1):
    print(gone)
    print(f"{i}. {pets}")

