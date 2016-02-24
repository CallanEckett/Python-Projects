from commands import *
from assets.player import *
from assets.places import *

from assets.container import *
from assets.items import *

player = Player("callan", 100, 50, 10, cell13)

def main(player):

	cell13.container.add(gold, 3)
	walkway.container.add(sword, 2)

	while not player.dead:
		line = str(input("> "))
		run(player, line)

main(player)