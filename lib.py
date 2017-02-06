import math


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
