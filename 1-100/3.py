# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def getPrimes():
	primes = [2,3]
	num = 3

	while True:
		num += 2
		isPrime = True
		for prime in primes:
			if num % prime == 0:
				isPrime = False
				break

		if isPrime:
			primes.append(num)
			yield num

def getPrimeFactors(val):
	primes = getPrimes()
	factors = []

	for prime in primes:
		print("Checking %d" % prime)

		if prime > val:
			break

		while val % prime == 0:
			val /= prime
			factors.append(prime)

	return factors

primeFactors = getPrimeFactors(600851475143)
print("Factors: %s" % primeFactors)
print("Largest Prime Factor: %d" % max(primeFactors))