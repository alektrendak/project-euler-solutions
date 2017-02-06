# https://projecteuler.net/problem=3
#
# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math

N = 600851475143


def fermat_factorization(n):
    if n == 2:
        return [n]
    a = math.ceil(math.sqrt(n))
    bb = a*a - n
    while not math.sqrt(bb).is_integer():
        a += 1
        bb = a*a - n
    return [k for results in (fermat_factorization(i) for i in [a - math.sqrt(bb), a + math.sqrt(bb)] if 1 < i < n)
            for k in results] or [n]


if __name__ == '__main__':
    print(max(fermat_factorization(N)))
