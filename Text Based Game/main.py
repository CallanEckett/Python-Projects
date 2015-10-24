from commands import *
from assets.player import *
from assets.places import *

player = Player("callan", 100, 50, 10)
player.location = cell

def main(player):

	while not player.dead:
		line = str(input("> "))
		run(player, line)

main(player)