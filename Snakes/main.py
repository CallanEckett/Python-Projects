from assets.player import *
from assets.board import *

if __name__ == '__main__':

	#Declaring the player/board objects

	game = board()
	game.title()

	playerOne = player(str(input("\nEnter the first players name: ")), game)
	playerTwo = player(str(input("Enter the second players name: ")), game)

	currentPlayer = playerOne

	#Main loop

	while True:

		print("\n{0}, it's your go!\n".format(currentPlayer.name))

		cmd = str(input("> "))

		#playerOne

		if not playerOne.nextPerson:

			playerOne.runCMD(cmd)
				
			if playerOne.nextPerson:

				playerOne.nextPerson = True; playerTwo.nextPerson = False
				currentPlayer = playerTwo

		#playerTwo

		elif not playerTwo.nextPerson:

			playerTwo.runCMD(cmd)
		
			if playerTwo.nextPerson:

				playerTwo.nextPerson = True; playerOne.nextPerson = False
				currentPlayer = playerOne