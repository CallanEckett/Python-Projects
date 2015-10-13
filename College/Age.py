while True:

	try:

		age = int(input("Please enter your age: "))

		if age < 13:
			print("You're still a child.")
		elif age >= 13 and age < 18:
			print("You're a teenager.")
		elif age >= 18:
			print("You're a adult now.")

		break

	except:

		print("Please enter a valid age.")
