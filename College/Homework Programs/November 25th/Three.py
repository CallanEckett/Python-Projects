#2D array containing the names, test 1 score & test 2 score
marks = [["James", 12, 15], ["George", 19, 17], ["Frank", 5, 21], ["Li", 25, 20], ["Amandeep", 21, 24]]

#Test 1 & 2 average variables
test1avg = 0; test2avg = 0

#Outputs the name, test 1 & 2 scores and the overall average for both tests
for x in marks:
	print("{0}: {1}: {2}: {3}".format(x[0], x[1], x[2], x[1] + x[2] / 2))

	#Add the current test 1 score to the average
	test1avg += x[1]
	#Add the current test 2 score to the average
	test2avg += x[2]

#Outputs the overall test 1 & 2 averages
print("Test 1 average: {0}\nTest 2 average: {1}".format(test1avg / len(marks), test2avg / len(marks)))