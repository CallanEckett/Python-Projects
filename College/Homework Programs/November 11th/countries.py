country = ["France", "UK", "Belgium", "Spain"]
capital = ["Paris", "London", "Brussels", "Madrid"]

#Program One

print("First country: {0}".format(country[0]))

#Program Two

print("\nThird country: {0}".format(country[2]))

#Program Three

print("\nCountries:\n")

for i in capital:
	print(i)

#Program Four

print("\nNumber of countries: {0}".format(len(capital)))

#Program Five

index = int(input("\nEnter an index number: "))

print("{0}: {1}".format(country[index], capital[index]))

#Program Six

print("\nCountry\tCapital\n")

for x, y in zip(country, capital):
	print("{0}\t{1}".format(x, y))

#Program Seven

nCountry = str(input("\nEnter a new country: "))
country.append(nCountry)

nCapital = str(input("Enter it's capital: "))
capital.append(nCapital)

print("\nCountry\tCapital")

for x, y in zip(country, capital):
	print("{0}\t{1}".format(x, y))

#Program Eight

dCountry = str(input("\nEnter the country you want to delete: "))

if dCountry in country:
	country.remove(dCountry)
else:
	print("{0} is not a valid country.".format(dCountry))

#Program Nine

print("\nFirst two countries: {0}".format(country[:2]))

#Program Ten

print("\nLast two countries: {0}".format(country[-2:]))

#Program Eleven

sCountry = str(input("\nEnter the country you want to search for: "))

cIndex = country.index(sCountry)
print(capital[cIndex])