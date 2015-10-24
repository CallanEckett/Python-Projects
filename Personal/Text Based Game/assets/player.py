from .entity import *
from .inventory import *

class Player(Entity):
	def __init__(self, name, health, stamina, damage):
		Entity.__init__(self, name, health)
		self.stamina = stamina
		self.damage = damage

		self.inventory = Container("inventory")