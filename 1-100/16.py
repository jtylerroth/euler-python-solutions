# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

val = 2**1000
str_val = str(val)

total = 0
for str_digit in str_val:
	total += int(str_digit)

print(total)