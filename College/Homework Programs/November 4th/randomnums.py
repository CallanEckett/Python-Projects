import random

nSevens = 0

for i in range(0, 10):
	print("")
	for n in range(0, 10):
		rNum = random.randint(0, 10)

		if rNum == 7:
			nSevens += 1

		print(rNum, end=" ")

print("\nNumber of sevens: {0}".format(nSevens))
