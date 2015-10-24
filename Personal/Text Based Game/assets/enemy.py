from .entity import *

class Enemy(Entity):
	def __init__(self, name, health, damage):
		Entity.__init__(self, name, health)
		self.damage = damage