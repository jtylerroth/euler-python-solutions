# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import math

def getPrimes():
	# Stolen from Euler #3, but properly yields the first primes
	primes = [2,3]
	num = 3

	yield 2
	yield 3

	while True:
		num += 2
		isPrime = True

		limit = math.sqrt(num)

		for prime in primes:
			if prime > limit:
				break

			if num % prime == 0:
				isPrime = False
				break

		if isPrime:
			primes.append(num)
			yield num

primes = getPrimes()

for i in range(0,10000):
	next(primes)

print(next(primes))
