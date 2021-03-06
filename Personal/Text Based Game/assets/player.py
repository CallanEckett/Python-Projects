from .entity import *
from .container import *
from .places import *

class Player(Entity):
	def __init__(self, name, health, stamina, damage, location=None):
		Entity.__init__(self, name, health)
		self.stamina = stamina
		self.damage = damage

		self.location = location

		self.inventory = Container("Inventory")

	def directions(self):
		directions = {
			"north": self.location.north,
			"south": self.location.south,
			"east": self.location.east,
			"west": self.location.west,
		}

		return directions