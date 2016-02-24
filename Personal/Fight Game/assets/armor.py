class Armor(object):
	def __init__(self, name, dMin, dMax):
		self.name = name
		self.raw = name.lower()

		self.dMin = dMin
		self.dMax = dMax