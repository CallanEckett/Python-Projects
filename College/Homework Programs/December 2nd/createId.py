def createId(firstname, middlename, surname):
	userId = "{0}{1}{2}".format(firstname[0], middlename[0], surname)
	return userId

f = str(input("Enter your first name: "))
m = str(input("Enter your middle name: "))
s = str(input("Enter your surname: "))

print(createId(f, m, s))