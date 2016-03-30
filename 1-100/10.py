# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import math

def getPrimes():
	# Stolen from Euler #7, but needed to be more efficient.
	# You only need to check up to the sqrt of the number
	primes = [2,3]
	num = 3

	yield 2
	yield 3

	while True:
		num += 2
		square = math.sqrt(num)
		isPrime = True
		for prime in primes:
			if num % prime == 0:
				isPrime = False
				break

			if prime > square:
				break

		if isPrime:
			primes.append(num)
			yield num

sum = 0

for prime in getPrimes():
	if prime > 2000000:
		break
	sum += prime

print(sum)
