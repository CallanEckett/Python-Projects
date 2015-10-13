while True:

	sex = str(input("Please enter your sex: "))

	if sex in ["M", "m", "MALE", "male"]:
		print("Mr")
		break
	elif sex in ["F", "f", "FEMALE", "female"]:
		print("Ms")
		break
	else:
		print("Please enter a valid sex.")