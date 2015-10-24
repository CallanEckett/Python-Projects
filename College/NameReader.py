name = str(input("Enter your name: "))

vowels = []
consonants = []

for x in name:
	if x in ["a", "e", "i", "o", "u"]:
		vowels.append(x)
	else:
		consonants.append(x)

print(vowels)
print(consonants)