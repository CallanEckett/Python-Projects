while True:

	password = str(input("Please enter a password: "))

	if len(password) >= 6:

		print("Your password is 6 characters or more, well done!")
		break

	else:

		print("Your password is less than 6 characters, get out...")