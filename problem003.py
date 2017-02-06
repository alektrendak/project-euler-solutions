# https://projecteuler.net/problem=3
#
# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from lib import fermat_factorization

N = 600851475143

if __name__ == '__main__':
    print(max(fermat_factorization(N)))
