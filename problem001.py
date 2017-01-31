# https://projecteuler.net/problem=1
#
# Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

N = 1000
FACTORS = [3, 5]


def sum_of_multiples_up_to_n(n, factors):
    return sum(i for i in range(1, n) if any(i % k == 0 for k in factors))


if __name__ == '__main__':
    print(sum_of_multiples_up_to_n(N, FACTORS))
