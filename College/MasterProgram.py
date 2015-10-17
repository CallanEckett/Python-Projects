class student(object):

	def __init__(self):
		pass

	def findInitials(self, forename, surname):
		self.initials = ("Your initials are definitely: {0}.{1}".format(forename[0].upper(), surname.capitalize()))
		print(self.initials)

	def findYear(self):
		if self.age < 16:
			print("Why are you even in college?")
		else:
			print("{0} years old eh, enjoy your time at college!".format(self.age))

	def findStudentID(self):
		if len(self.studentID) == 6:
			if "h" in self.studentID.lower():
				print("'H' in your ID number, you must be a student.")
			else:
				print("No 'H' in your ID number, you must be a teacher.")
		else:
			print("You must have entered your ID wrongly, there should be 6 characters.")

forename = input(": ")


x = student()
x.findInitials(forename, "eckett")
