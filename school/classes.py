class Character:
	def __init__(self, health, damage, speed):
		self.health = health
		self.damage = damage
		self.speed = speed
	def double_speed(self):
		self.speed *= 2
		
warrior = Character(100, 50, 10)

warrior.double_speed()

print(f"Warrior speed: {warrior.speed}")