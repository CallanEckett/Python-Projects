from assets.objects import *

#Functional functions

def run(cPlayer, line):
	cmd = line.split()

	if cmd[0] not in commands:
		print("{0} is not a valid command".format(cmd[0]))
	else:
		commands[cmd[0]](cPlayer)

def swap(cPlayer, array):
	pass

#Game Functions

def test(cPlayer):
	cPlayer.goes += 1
	swap(cPlayer, players)

commands = {
	"test": test
}