word = str(input("Please enter a word: "))

print("Caps: {0}".format(word.upper()))
print("Length of word: {0}".format(len(word)))
print("First character: {0}".format(word[0]))

if len(word) >= 5:
	print("Third, fourth and fifth characters: {0}".format(word[2:5]))
else:
	print("Third, fourth and fifth characters: word is only {0} characters long".format(len(word)))

if len(word) >= 3:
	print("Last three characters: {0}".format(word[-3:]))
else:
	print("Last three characters: word is only {0} characters long".format(len(word)))