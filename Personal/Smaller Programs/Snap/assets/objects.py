from .player import *
from .game import *

#Players: name - goes

p1 = Player("p1", 0)
p2 = Player("p2", 0)

players = [p1, p2]

#Game: name - current player

game = Game("Game", p1)