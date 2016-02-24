def triangleArea(base, height):
	area = 0.5 * base * height
	return area

b = float(input("Enter the base of the triangle: "))
h = float(input("Enter the height of the triangle: "))

print("Triangle area: {0}".format(triangleArea(b, h)))