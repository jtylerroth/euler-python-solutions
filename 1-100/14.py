# The following iterative sequence is defined for the set of positive integers:
# 
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# 
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Dictionary will hold all the known answers to speed up calculations
lengths = {}

def collatzSequence(n):
	length = 1

	while n != 1:
		if n % 2 == 0: # even
			n = n/2
		else:		   # odd
			n = 3*n+1
		
		length += 1
		if n in lengths:
			length += lengths[n]
			break # already solved

	return length

# Question example
# print(collatzSequence(13))

max_n = 1
max_val = 1

for i in range(1,1000000):
	seq = collatzSequence(i)
	lengths[i] = seq # Save the answer

	if seq > max_val:
		max_n = i
		max_val = seq

print("Longest chain: {0} with length {1}".format(max_n,max_val))
