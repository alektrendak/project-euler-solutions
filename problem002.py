# https://projecteuler.net/problem=2
#
# Even Fibonacci numbers
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

MAX_VAL = 4000000


def fibonacci_generator(max_val):
    i, j = 0, 1
    while True:
        if i > max_val:
            raise StopIteration
        yield i
        i, j = j, i + j


def sum_of_even_fibonacci_numbers_up_to_n(n):
    return sum(k for k in fibonacci_generator(n) if k % 2 == 0)


if __name__ == '__main__':
    print(sum_of_even_fibonacci_numbers_up_to_n(MAX_VAL))