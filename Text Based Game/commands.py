import os

from assets.player import *
from assets.container import *
from assets.items import *

#Functional functions

def run(player, line):
	cmd = line.split()

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

def clear(player):
	if os.name == "posix":
		os.system("clear")
	elif os.name == "dos":
		os.system("cls")

def close(player):
	exit()

def directions(player):
	directions = {
		"north": player.location.north,
		"south": player.location.south,
		"east": player.location.east,
		"west": player.location.west
	}

	return directions


#Item Functions

def inventory(player):
	if len(player.inventory) > 0:
		for name, item in player.inventory:
			print("{0}: {1}".format(item.name, item.quantity))
	else:
		print("Inventory is empty.")

def take(player, item, quantity=1):
	player.inventory.add(eval(item), int(quantity))

def drop(player, item, quantity=1):
	player.inventory.remove(eval(item), int(quantity))

def openx(player, openable):
	pass

def put(player, item, container):
	pass

#Movement Functions

def go(player, direction):

	if direction in directions(player):

		entrance = directions(player)[direction].entrance

		if entrance.unlocked:
			player.location = directions(player)[direction]
		else:
			print("The {0} is locked.".format(entrance.name))

	else:
		print("I can't go {0}".format(direction))

def look(player, direction):

	if direction in directions(player):
		print(directions(player)[direction].name)

def check(player):
	print("{0}: {1}".format(player.location.name, player.location.desc))

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
	"check": check 
}
