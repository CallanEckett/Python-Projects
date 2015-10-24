class Place(object):
	def __init__(self, name, desc):
		self.name = name
		self.desc = desc

		self.north = None
		self.east = None
		self.south = None
		self.west = None

		self.cutscene = None

	def connect(self, north=None, east=None, south=None, west=None):
		self.north = north
		if north:
			north.south = self
		self.south = south
		if south:
			south.north = self
		self.east = east
		if east:
			east.west = self
		self.west = west 
		if west:
			west.east = self

	def cutscene(self, cutscene):
		self.cutscene = cutscene
