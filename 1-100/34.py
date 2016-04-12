# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def factorial(n):
	if n == 0:
		return 1
	if n == 1:
		return 1
	return n * factorial(n-1)

def digits(n):
	while n != 0:
		yield int(n % 10)
		n = int(n / 10)

factorials = []

# prepopulate the list of factorials
for i in range(0,10):
	factorials.append(factorial(i))

curious = []
curious_sum = 0

for i in range(10, 100000):
	sum = 0
	for digit in digits(i):
		sum = sum + factorials[digit]

	if sum == i:
		curious.append(i)
		curious_sum = curious_sum + i

print("Curious Numbers: {0}, Sum: {1}".format(curious, curious_sum))