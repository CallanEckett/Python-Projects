def addInterest(amount):
	plusInterest = amount * 1.10
	return plusInterest

a = int(input("What is the original amount: "))
print(plusInterest(a))