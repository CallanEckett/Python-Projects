def calc(num, num2):
	addition =  num + num2
	multiplication = num * num2
	subtraction = num - num2
	division = num / num2

	return(addition, multiplication, subtraction, division)

while True:

	number = int(input("Enter a number: "))
	number2 = int(input("Enter a second number: "))

	if str(number) == "exit" == str(number2):
		exit()

	add, mul, sub, div = calc(number, number2)

	commands = {"+": add,
				"*": mul,
				"-": sub,
				"/": div}

	x = str(input("What operator do you want: "))

	if x in commands:
		print(commands.get(x))
	elif x.lower() == "exit":
		exit()
	else:
		print("Incorrect Value.")