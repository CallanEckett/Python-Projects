class Entity(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

		self.dead = False

	def update(self):
		if self.health <= 0:
			self.dead = True; self.health = 0