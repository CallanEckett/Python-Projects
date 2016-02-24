class Weapon(object):
	def __init__(self, name, aMin, aMax):
		self.name = name
		self.raw = name.lower()

		self.aMin = aMin
		self.aMax = aMax