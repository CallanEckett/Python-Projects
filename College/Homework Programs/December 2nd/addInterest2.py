def addInterest2(amount, rate):
	plusInterest = amount * (1 + rate / 100)
	return plusInterest

a = int(input("Enter the original amount: "))
r = int(input("Enter the percentage increase: "))

print(plusInterest(a, r))
