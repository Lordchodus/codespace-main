class Character:
	def __init__(self, health, damage, speed):
		self.health = health
		self.damage = damage
		self.speed = speed
	def double_speed(self):
		self.speed *= 2
		
warrior = Character(100, 50, 10)

class Enemy:
	def __init__(enemy, health, damage, speed):
		enemy.health = health
		enemy.damage = damage
		enemy.speed = speed
	def double_speed(enemy):
		enemy.speed *= 2
		
Wolf = Enemy(10, 5, 15)

player = input("Enter your character's name: ")

if player:
    print(f"Welcome, {player}!")

gamestart = input("Do you want to start the game? (yes/no): ").lower()
if gamestart == "yes":
    print("You find yourself in a dark forest.")
    action = input("Do you want to go left or right? ").lower()
    if action == "left":
        print("You encounter a wild beast!")
        fight = input("Do you want to fight or run? ").lower()
        if fight == "fight":
            print(input("Type attack to attack the beast. "))
            attack = input().lower()
            if attack == "attack":
                print("You defeated the beast!")
			