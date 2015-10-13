while True:

	numbers = []

	try:

		for x in range(0, 3):

			current =  int(input("Please enter a number: "))
			numbers.append(current)

	except:

		print("Please enter valid numbers.")
		numbers.clear()

	if len(numbers) == 3:
		biggest = max(numbers)
		print(biggest)
		break