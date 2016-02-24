#Initial list creation
colors = ["red", "black", "orange"]

#Appending new items to the list
for c in ("yellow", "green", "blue", "indigo", "violet"):
	colors.append(c)

#Removing the color black from the list
colors.remove("black")

#Outputting the third element
print("Third element: {0}".format(colors[2]))

#Outputting the length of the list
print("Length of the list: {0}".format(len(colors)))

#Outputting the first four elements of the list
print("First four list elements: {0}".format(colors[:4]))

#Outputting the last 3 elements of the list
print("Last three list elements: {0}".format(colors[-3:]))

#User chosen element
elements = int(input("What number do you want: "))
print("You have chosen: {0}".format(colors[elements]))

#Prints the entire list
print("Entire list: {0}".format(colors))

#Prints the entire list with spaces inbetween
for e in colors:
	print(e, end=" ")

print("\n")