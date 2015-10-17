import random

#Declaring player class

class player(object):
	def __init__(self, name="default", current=1, nextPerson=False, dice=0):
		self.name = name
		self.current = current
		self.nextPerson = nextPerson
		self.dice = dice

	def roll(self):
		self.dice = random.randint(1, 6)
		self.current += self.dice

		if self.dice != 0:
			self.nextPerson = True
		else:
			print("You haven't rolled yet!")

	def wonGame(self):
		if self.current >= 15:
			print("{0} has won the game!".format(self.name))
			exit()

	def landed(self):
		if self.current in snakes:
			
			self.current = snakes[self.current]

			print("{0} has landed on a snake, they're now on {1}".format(self.name, self.current))
			self.wonGame()
		elif self.current in ladders:

			self.current = ladders[self.current]

			print("{0} has landed on a ladder, they're now on {1}".format(self.name, self.current))
			self.wonGame()

	def list(self):
		self.available = [
		("roll", "rolls the dice."),
		("exit", "exits the game."),
		("list", "list of available commands\n")]

		for x, y in self.available:
			print("{0}: {1}".format(x, y))

	def exit(self):
		exit()

	def runCMD(self, cmd):
		commands = {
		"roll": self.roll,
		"list": self.list,
		"exit": self.exit}

		if cmd in commands:
			commands[cmd]()
		else:
			print("{0} is an invalid command.".format(cmd))

#Main code.

if __name__ == '__main__':

	#Declaring the player objects

	playerOne = player(str(input("Enter the first players name: ")))
	playerTwo = player(str(input("Enter the second players name: ")))

	currentPlayer = playerOne

	#Declaring the snakes & ladders

	snakes = {
	13: 6,
	27: 15,
	44: 34
	}
	ladders = {
	4: 15,
	39: 54
	}

	#Main loop

	while True:

		print("\n{0}, it's your go!\n".format(currentPlayer.name))

		cmd = str(input("> "))

		#playerOne

		if not playerOne.nextPerson:

			playerOne.runCMD(cmd)
				
			if playerOne.nextPerson:

				print("Player {0} rolled a {1}, they're now on square {2}".format(playerOne.name, playerOne.dice, playerOne.current))

				playerOne.nextPerson = True; playerTwo.nextPerson = False
				currentPlayer = playerTwo

				playerOne.wonGame()
				playerOne.landed()

		#playerTwo

		elif not playerTwo.nextPerson:

			playerTwo.runCMD(cmd)
		
			if playerTwo.nextPerson:

				print("Player {0} rolled a {1}, they're now on square {2}".format(playerTwo.name, playerTwo.dice, playerTwo.current))

				playerTwo.nextPerson = True; playerOne.nextPerson = False
				currentPlayer = playerOne

				playerTwo.wonGame()
				playerTwo.landed()