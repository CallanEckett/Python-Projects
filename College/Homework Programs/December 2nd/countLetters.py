def countLetters(letter, word):
	noLetters = 0

	for i in word:
		if i == letter:
			noLetters += 1

	return noLetters

l = str(input("What letter do you want to test for: "))
w = str(input("What word would you like to test: "))

print(countLetters(l, w))