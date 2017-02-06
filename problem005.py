# https://projecteuler.net/problem=5
#
# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


# Solution comment:
# We're looking for multiple of numbers in set of common prime factors of numbers in given range

from collections import Counter
from functools import reduce
from operator import mul, or_

from lib import fermat_factorization

N = 20


def smallest_multiple(n):
    return reduce(mul, reduce(or_, [Counter(fermat_factorization(i)) for i in range(2, n + 1)]).elements())


if __name__ == '__main__':
    print(smallest_multiple(N))
