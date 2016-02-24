name = str(input("Enter your name: "))

vowels = []
consonants = []

for i in name:
	if i in "aeiou":
		vowels.append(i)
	else:
		consonants.append(i)

print("Vowels: {0}\nConsonants: {1}".format(" ".join(vowels), " ".join(consonants)))