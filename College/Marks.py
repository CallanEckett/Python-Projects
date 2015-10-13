while True:

	try:

		mark = int(input("Enter a mark: "))

		if mark >= 0 and mark <= 100:

			if mark >= 70:
				print("Distinction")
			elif mark >= 60 and mark < 70:
				print("Merit")
			elif mark >= 50 and mark < 60:
				print("Pass")
			else:
				print("Fail")

			break

		else:

			print("Please enter a mark between 0 and 100.")

	except:

		print("Please enter a valid number.")