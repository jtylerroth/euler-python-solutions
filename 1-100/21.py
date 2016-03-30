# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# 
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper # divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.# 
# 
# Evaluate the sum of all the amicable numbers under 10000.

def getProperDivisors(n):
	divisors = []

	for i in range(1, int(n/2+1)):
		if n % i == 0:
			divisors.append(i)

	return divisors

sums = []
sums.append(0) # Unused 0 index, to keep things simple

# Precalculate all the proper divisor sums
for i in range(1,10000):
	sums.append(sum(getProperDivisors(i)))

total = 0

for i in range(1,10000):
	for j in range(i+1,10000):
		if sums[i] == j and sums[j] == i:
			total += i
			total += j

print(total)