# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# 
# Let us list the factors of the first seven triangle numbers:
# 
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# 
# What is the value of the first triangle number to have over five hundred divisors?

import math

def triangleNumbers():
	sum = 0
	val = 0

	while True:
		val += 1
		sum += val
		yield sum

def numberOfPrimes(n):
	divisors = 0
	limit = math.sqrt(n)

	if limit.is_integer():
		divisors += 1

	for i in range(1, int(limit)):
		if n % i == 0:
			# account for upper and lower divisor
			divisors += 2

	return divisors

for n in triangleNumbers():
	if numberOfPrimes(n) > 500:
		print(n)
		break