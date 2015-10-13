while True:

	try:

		number = int(input("Please enter a number: "))

		if number >= 1 and number <= 20:
			print("Yes")
		else:
			print("No")

		break

	except:

		print("Please enter a valid number.")