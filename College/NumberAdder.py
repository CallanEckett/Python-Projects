numbers = []

number = int(input("Enter a number, enter -1 to finish: "))

while number != -1:
	numbers.append(number)
	number = int(input("Enter another number, enter -1 to finish: "))

print("\nThe maximum value entered is {0},\nThe minimum value entered is {1}".format(max(numbers), min(numbers)))