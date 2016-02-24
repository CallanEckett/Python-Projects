def palindrome(p):
	pass

if __name__ == "__main__":
	string = str(input("Enter a block palindrome: "))
	while len(string) < 2 or len(string) > 10:
		string = str(input("Enter a valid block palindrome: "))

	palindrome(string)