from random import randint

number = randint(1, 100)

guess = 0

while guess != number:
	guess = int(input("Guess a number: "))

	if guess > number:
		print("Your guess of {0} is higher than the number!".format(guess))
	elif guess < number:
		print("Your guess of {0} is lower than the number!".format(guess))
	else:
		print("You guessed correctly, the number was {0}!".format(number))
		break