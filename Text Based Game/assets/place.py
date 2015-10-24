from .entrances import *

class Place(object):
	def __init__(self, name, desc, entrance=None):
		self.name = name
		self.desc = desc
		self.entrance = door

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

	def scene(self, cutscene):
		self.cutscene = cutscene