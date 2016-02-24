tt = int(input("What times table would you like to print: "))

for i in range(1, 13):
	print("{0} X {1} = {2}".format(i, tt, i*tt))