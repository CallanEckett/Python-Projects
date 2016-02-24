import os

from assets.player import *
from assets.container import *
from assets.items import *
from assets.entrances import *

#Functional functions

def run(player, line): #temporary, need to find stable solution
	cmd = line.split()
	cmd = [element.lower() for element in cmd]

	try:
		if cmd[0] not in commands:
			print("Invalid Command.")
		elif len(cmd) == 1:
			commands[cmd[0]](player)
		elif len(cmd) == 2:
			commands[cmd[0]](player, cmd[1])
		elif len(cmd) == 3:
			commands[cmd[0]](player, cmd[1], cmd[2])
		elif len(cmd) == 4:
			commands[cmd[0]](player, cmd[1], cmd[2], cmd[3])

	except TypeError:
		print("Error")

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

#Item Functions

def inventory(player):

	#Contains the players inventory
	pi = player.inventory

	#If the inventory has atleast one item inside
	if len(pi) > 0:
		for name, item in pi:
			print("{0}: {1}".format(item.name, item.quantity))

	#If the inventory has no items
	else:
		print("Inventory is empty.")

def take(player, item, quantity=1): #Need to get working with containers

	#Contains the players inventory
	pi = player.inventory

	#If the item exists
	try:
		pi.add(eval(item), int(quantity))

	#If the item doesn't exist
	except NameError:
		print("There is no {0} in here.".format(item))

def drop(player, item, quantity=1): #Need to get working with containers

	#Contains the players inventory
	pi = player.inventory

	try:
		pi.remove(eval(item), int(quantity))

	#If the item doesn't exist
	except NameError:
		print("There is no {0} in here.".format(item))

def openx(player, openable):
	pass

def put(player, item, container):
	pass

#Movement Functions

def go(player, direction):

	#Contains all the available directions
	pd = player.directions()

	#Checks if the direction is in the available directions
	if direction in pd:

		#If there is something in the direction
		try:
			entrance = pd[direction].entrance

			if entrance.unlocked:
				player.location = pd[direction]
				print("You are now in the {0}.".format(player.location.name))
			else:
				print("The {0} is locked.".format(entrance.name))

		#If there is nothing in the direction (Nonetype)
		except AttributeError:
			print("I can't go {0}".format(direction))

def look(player, direction):

	#Contains all the available directions
	pd = player.directions()

	#Checks if the direction is in the available directions
	if direction in pd:

		#If there is something in the direction
		try:
			print("There is a {0} to the {1}.".format(pd[direction].name, direction))

		#If there is nothing in the direction (Nonetype)
		except AttributeError:
			print("There is nothing to the {0}.".format(direction))

	#If the player wants to look around their current location
	if direction == "around":

		#Prints the direction, and name of the locations
		for i in pd:
			if pd[i] != None:
				print("{0}: {1}".format(i.capitalize(), pd[i].name))

#Creator commands

def addItem(player, item, quantity):

	player.location.container.add(eval(item), eval(quantity))

def roomInv(player):

	for name, item in player.location.container:
			print("{0}: {1}".format(item.name, item.quantity))

#List of Commands

commands = {
	"clear": clear,
	"exit": close,
	"i": inventory,
	"take": take,
	"drop": drop,
	"open": openx,
	"go": go,
	"look": look,
	"add": addItem,
	"roominv": roomInv
}