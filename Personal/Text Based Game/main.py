from assets.player import *
from assets.commands import *
from assets.place import *
from assets.cutscene import *

commands = {"tester": tester}

player = Player("callan", 100, 50, 10)

p = Place("house", "home")
x = Cutscene("You are in a house")
p.cutscene(x)

def runCmd(cmd, args, player):
	if cmd in commands:
		commands[cmd](player, args)
	else:
		print("{0}, isn't a valid command.".format(cmd))

def main(player):

	while not player.dead:
		line = str(input("> "))
		cmd = line.split()
		cmd.append("default")

		runCmd(cmd[0], cmd[1], player)

main(player)

