import os, random

from assets.game import *
from assets.items import *

#Base functions

def run(game, line):
	cmd = line.split()

	if cmd[0] not in commands:
		print("{0}, is an invalid command".format(cmd[0]))
	elif len(cmd) == 1:
		commands[cmd[0]](game.current)
	elif len(cmd) == 2:
		commands[cmd[0]](game.current, cmd[1])

def swap(player): #Need to refine, preferably with dictionaries
	players.reverse()
	game.current = players[0]

def find(player, array, check):
	for i in array:
		if check == i.raw:
			return i

	return False

def generator(player, a, b):
	return random.randint(a, b)

#Starting functions

def gAttr(player):
	for p in players:

		#Setting the current players name
		name = str(input("Enter your name: "))
		p.name = name
		p.raw = name.lower()

		#Setting the current players weapon
		wep = str(input("Choose your weapon: "))

		while not find(p, weapons, wep):
			wep = str(input("Choose another weapon: "))
		
		p.weapon = find(p, weapons, wep)

#Console functions

def commands(player): #Need to write, prints list of commands and their functions
	pass	

def clear(player):
	#If the OS is linux based
	if os.name == "posix":
		os.system("clear")

	#If the OS is windows based
	elif os.name == "dos":
		os.system("cls")

def close(player):
	#Exits the game
	exit()

#Game functions

def attack(player, target):
	#Target for the attack
	t = find(player, players, target)

	if t == player:
			#This is so the current player can't damage themselves
			print("You can't attack yourself.")
	else:
		#Generates a random damage value based on the players weapon
		dam = generator(player, player.weapon.aMin, player.weapon.aMax)

		#Takes away the damage value generated from the targets health
		t.health -= dam

		#Statement verifying the target has been damaged
		print("{0} has been hit for {1} points, and now has {2} health".format(t.name, dam, t.health))

		#Swaps the current player to the target
		swap(player)

'''
	#Damages the target
	try:
		if t == player:
			#This is so the current player can't damage themselves
			print("You can't attack yourself.")
		else:
			#Generates a random damage value based on the players weapon
			dam = generator(player, player.weapon.aMin, player.weapon.aMax)

			#Takes away the damage value generated from the targets health
			t.health -= dam

			#Statement verifying the target has been damaged
			print("{0} has been hit for {1} points, and now has {2} health".format(t.name, dam, t.health))

			#Swaps the current player to the target
			swap(player)

	#If an incorrect player name is entered
	except AttributeError:
		print("There is no player named {0}".format(target))
'''

def defend(player):
	pass

commands = {
	"attack": attack,
	"defend": defend,
	"clear": clear,
	"close": close,
	"commands": commands
}