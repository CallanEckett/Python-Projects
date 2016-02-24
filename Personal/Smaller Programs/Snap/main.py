from commands import *
from assets.objects import *

def main(cPlayer):
	while not cPlayer.won:
		line = str(input("> "))
		run(cPlayer, line)

main(game.cPlayer)