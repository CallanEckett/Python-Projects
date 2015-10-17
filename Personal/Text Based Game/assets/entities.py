class entity(object):
	def __init__(self, name, health, alive):
		self.name = name
		self.health = health
	
		self.alive = alive

	def isAlive(self):
		if self.health <= 0:
			self.alive = False
		else:
			self.alive = True

		return self.alive

class enemy(entity):
	def __init__(self, name, health, damage, alive):
		super(enemy, self).__init__(name, health, alive)
		self.damage = damage

class player(entity):
	def __init__(self, name, health, damage, alive):
		super(player, self).__init__(name, health, alive)
		self.damage = damage

