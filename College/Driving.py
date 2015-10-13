while True:

	try:

		age = int(input("Please enter your age: "))

		if age >= 17:
			print("Congrats, you can drive!")
		else:
			print("I'm afraid you can't drive...")

		break

	except: 

		print("Please enter a valid age.")