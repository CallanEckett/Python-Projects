class Player(object):
	def __init__(self, name, health, weapon, armor):
		self.name = name
		self.raw = name.lower()
		self.health = health

		self.weapon = weapon
		self.armor = armor

		self.dead = False

	def update(self):
		if self.health <= 0:
			self.dead = True; self.health = 0