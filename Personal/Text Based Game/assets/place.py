from .entrances import *

class Place(object):
	def __init__(self, name, desc, container, entrance):
		self.name = name
		self.desc = desc
		self.container = container
		self.entrance = entrance

		self.north = None
		self.east = None
		self.south = None
		self.west = None

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