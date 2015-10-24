import os

def clear(player, lines=100):
	if os.name == "posix":
		os.system("clear")
	elif os.name in ["dos"]:
		os.system("cls")
	else:
		print("\n"*lines)

def tester(player, *args):
	print("this is a tester")
