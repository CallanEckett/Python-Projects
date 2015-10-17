inventory = {}

def pickup(item):

	if item not in inventory:
		inventory[item] = 1
	else:
		inventory[item] += 1

def drop(item):

	if item in inventory:
		if inventory[item] == 1:
			del inventory[item]
			print("You dropped, {0}".format(item))
		elif inventory[item] > 1:
			inventory[item] -= 1
	else:
		print("{0}, not in inventory".format(item))

def inventoryCheck(*args):
	return inventory
	