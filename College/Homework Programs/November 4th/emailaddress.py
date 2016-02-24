email = str(input("Enter an email address: "))

at = 0

for i in email:
	if i in "@.":
		if i == "@":
			at += 1
	