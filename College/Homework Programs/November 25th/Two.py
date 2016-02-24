#List containing the marks
marks = [12, 19, 5, 25, 21]

#List containing the names
names = ["James", "George", "Frank", "Li", "Amandeep"]

#Added up score variable
added = 0

#adds up the score & finds the average
for m in marks:
	added += m
	average = added / len(marks)

#Outputs the average score
print("Average score: {0}".format(average))

#Need to find how to do the above in one line

print("maximum: {0}, minimum: {1}".format(max(marks), min(marks)))

#Output format
print("name: test score: average score")

#Outputs the names, test score & average score
for n in names:
	m = marks[names.index(n)]
	print("{0}: {1}: {2}".format(n, m, m / 25 * 100))