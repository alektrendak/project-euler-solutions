# https://projecteuler.net/problem=4
#
# Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


# Solution comment:
# Palindrome we're looking for is in form abccba, so can be written as sum
# 10001*a + 10010*b + 1100*c == 11(9091a + 910b + 100c)
# It has to be dividable by 11, so at least one multiplier has to be dividable by 11 (because it's prime)
# From this point it's pure brute force:


def find_three_digit_multipliers_palindrome():
    k = 999
    l = 990  # largest dividable by 11
    max_palindrome = 0
    while k >= 100 and l >= 100:
        product = k * l
        if product > max_palindrome and str(product) == str(product)[::-1]:
            max_palindrome = product

        if k > 100:
            k -= 1
        else:
            k = 999
            l -= 11
    return max_palindrome


if __name__ == '__main__':
    print(find_three_digit_multipliers_palindrome())
