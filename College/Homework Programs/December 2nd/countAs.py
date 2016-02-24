def countAs(word):
	noAs = 0

	for i in word:
		if i == "a":
			noAs += 1

	return noAs

w = str(input("What word do you want to test: "))
print(countAs(w))