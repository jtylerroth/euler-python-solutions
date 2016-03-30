# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisors = range(2,20)
current = 2520

while (all(current % i == 0 for i in divisors) == False):
	current += 20 # must be divisible by 20, no point in checking in between

print(current)