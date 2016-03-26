# Let a0, a1, a2, ... be an integer sequence defined by:
#
# a0 = 1;
# for n ≥ 1, an is the sum of the digits of all preceding terms.
# The sequence starts with 1, 1, 2, 4, 8, 16, 23, 28, 38, 49, ...
# You are given a10^6 = 31054319.
#
# Find a10^15.


def sum_digits(i):
    a = 1
    n = 1
    while n < i:
        s = str(a)
        for ch in s:
            a += int(ch)
        n += 1
    return a

# Proof function outputs example correctly
print('Example - ' + str(sum_digits(10 ** 6)))
# Answer to the question
print('Answer - ' + str(sum_digits(10 ** 15)))


