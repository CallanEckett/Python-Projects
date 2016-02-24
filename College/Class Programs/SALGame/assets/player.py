import random, os

class player(object):
	def __init__(self, name, board):
		self.name = name
		self.board = board

		self.current = 1
		self.nextPerson = False

	def roll(self):
		self.dice = random.randint(1, 6)
		self.current += self.dice

		if not self.landed():

			print("Player {0} rolled a {1}, they're now on square {2}".format(self.name, self.dice, self.current))

		elif self.current in self.board.snakes:
			self.current = self.board.snakes[self.current]

			print("Player {0} rolled a {1} and landed on a snake!, they're now on square {2}".format(self.name, self.dice, self.current))
		elif self.current in self.board.ladders:
			self.current = self.board.ladders[self.current]

			print("Player {0} rolled a {1} and landed on a ladder!, they're now on square {2}".format(self.name, self.dice, self.current))

		if self.current >= 15:
			print("{0} has won the game!".format(self.name))
			exit()

		self.nextPerson = True

	def list(self):
		self.available = [
		("roll", "rolls the dice."),
		("clear", "clears the screen."),
		("exit", "exits the game."),
		("list", "list of available commands.\n")
		]

		for x, y in self.available:
			print("{0}: {1}".format(x, y))

	def clear(self):
		if os.name == "posix":
			os.system("clear")
		else:
			os.system("cls")

	def exit(self):
		exit()

	def landed(self):
		if self.current in self.board.snakes or self.current in self.board.ladders:
			return True
		else:
			return False

	def runCMD(self, cmd):
		commands = {
		"roll": self.roll,
		"clear": self.clear,
		"exit": self.exit,
		"list": self.list
		}

		if cmd in commands:
			commands[cmd]()
		else:
			print("{0} is an invalid command.".format(cmd))