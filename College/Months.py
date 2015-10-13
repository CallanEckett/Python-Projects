months = {
1: "January",
2: "February",
3: "March",
4: "April",
5: "May",
6: "June",
7: "July",
8: "August",
9: "September",
10: "October",
11: "November",
12: "December"
}

while True:

	try:

		number = int(input("Please enter the number of a month: "))

		if number > 0 and number <= 12:

			print(months.get(number))

			break

		else:
			print("Please enter a number between 1 and 12.")

	except:

		print("Please enter a valid number.")

	