while True:

	try:

		number = int(input("Please enter a number: "))

		if "-" in str(number):
			print("The number given is negative.")
		else:
			print("The number given is posative")

		break

	except:

		print("Please enter a valid number.")