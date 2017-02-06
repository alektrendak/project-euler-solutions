import gmpy2


def fermat_factorization(n):
    if n <= 3:
        return [n]
    if n % 2 == 0:
        return [2] + fermat_factorization(n//2)
    a = gmpy2.isqrt(n)
    if a * a == n:
        return [int(a), int(a)]
    else:
        a += 1
    b2 = gmpy2.square(a) - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = a*a - n
    b = gmpy2.isqrt(b2)
    return [int(k) for results in (fermat_factorization(i) for i in [a - b, a + b] if 1 < i < n)
            for k in results] or [int(n)]
