number = int(input("Which number do you want: "))

for x in range(1, 13):
	print("{0} x {1} = {2}".format(x, number, x*number))