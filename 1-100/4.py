# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(val):
	string = str(val)
	return string == string[::-1]

def getLargestPalindrome():
	first = 999
	second = 999

	largest = 0

	# Iterating backwards probably makes it slightly faster for branch prediction maybe.
	for i in range(999, 100, -1):
		for j in range(999, 100, -1):
			val = i*j
			if isPalindrome(val) and val > largest:
				largest = val

	return largest

print(getLargestPalindrome())