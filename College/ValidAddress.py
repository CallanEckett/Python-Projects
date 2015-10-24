email = str(input("Enter an email address: "))

characters = {
	"@": 0,
	".": 0
}

for x in email:
	if x == "@":
		characters[x] += 1
	elif x == ".":
		characters[x] += 1
	else:
		pass

if characters["@"] == 1 and characters["."] >= 1:
	print("The address is valid.")
else:
	print("The address is not valid.")