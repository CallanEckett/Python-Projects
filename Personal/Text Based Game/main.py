from assets.entities import *
from assets.inventory import *
from assets.commands import *

commands = {"pickup": pickup,
			"drop": drop,
			"inventory": inventoryCheck,
			"check": checkAlive}

def main():
	while True:

		cmdLine = str(input("> "))
		cmd, args = splitCommand(cmdLine)
		
		if cmd in commands:
			commands[cmd](args)
		else:
			print("{0}, is not a valid command.".format(cmd))

def splitCommand(cmd):

	cmdSplit = cmd.split()

	if len(cmdSplit) == 1:
		cmd, args = cmdSplit[0], "default"
	else:
		cmd, args = cmdSplit[0], cmdSplit[1]

	return cmd, args

if __name__ == '__main__':
	p = player("callan", 100, 10, True)

	main()