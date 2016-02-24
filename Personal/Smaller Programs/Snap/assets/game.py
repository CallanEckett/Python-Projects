class Game(object):
	def __init__(self, name, cPlayer):
		self.name = name
		self.cPlayer = cPlayer

	def setPlayer(self, player):
		self.cPlayer = player