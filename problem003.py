# https://projecteuler.net/problem=3
#
# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import itertools
import math

N = 600851475143


def fermat_factorization(n):
    a = math.ceil(math.sqrt(n))
    bb = a*a - n
    while not math.sqrt(bb).is_integer():
        a += 1
        bb = a*a - n
    return list(itertools.chain.from_iterable(filter(
        lambda x: x != [1],
        [k for k in (fermat_factorization(i) if (i > 1 and i != n) else [i]
                     for i in [a - math.sqrt(bb), a + math.sqrt(bb)])]
    )))


if __name__ == '__main__':
    print(max(fermat_factorization(N)))
