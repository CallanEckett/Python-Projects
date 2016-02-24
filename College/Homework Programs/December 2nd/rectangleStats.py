def rectangleStats(length, width):
	area = length * width
	perimeter = 2 * length + 2 * width

	return area, perimeter

l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))

print(rectangleStats(l, w))