from random import randint

sevens = 0

for x in range (1, 11):
	for y in range(1, 11):
		number = randint(1, 100)

		if number == 7:
			sevens += 1

		print("{0}, ".format(number), end="")
	print("\n ")

print("There are {0} seven(s)".format(sevens))