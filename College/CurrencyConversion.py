print("£\t$\teuros")

for x in range(10, 101, 10):
	dollars = x*1.5974 
	euros = x*1.3670

	print("{0}\t{1:.2f}\t{2:.2f}".format(x, dollars, euros))


