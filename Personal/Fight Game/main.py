from commands import *

from assets.game import *
from assets.items import *

def main(p1, p2):

	gAttr(game.current)

	while not p1.dead and not p2.dead:
		print("{0} it's your go.".format(game.current.name)) #Preferably needs to be refined

		line = str(input("> "))
		run(game, line)

main(p1, p2)