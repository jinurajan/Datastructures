"""
split the numbers into first and second half

eg 5678, 1234
a = 56, b = 78
c = 12 d = 34

1) ac
2) ad
3) bc
4) bd

return 10 raised to n * ac + 10 raised n/2 *(ad+bc) + bd

Please not that multiply_optimized and method karatsuba only work in python 2.7 because of the division changes

"""


def multiply(m, n):
    l = len(str(m))
    if l == 1:
        return m * n
    else:
        a, b = int(m / pow(10, l//2)), m % pow(10, l//2)
        c , d = int(n / pow(10, l//2)), n % pow(10, l//2)
        ac = multiply(a, c)
        ad = multiply(a, d)
        bc = multiply(b, c)
        bd = multiply(b, d)
        return pow(10, l) * ac + (pow(10, l//2) * (ad + bc)) + bd


def multiply_optimized(m, n):
    """
    Method fails for integers with different length
    """
    if len(str(m)) == 1 or len(str(n)) == 1:
        return m * n
    else:
        l = max(len(str(m)),len(str(n)))
        lby2 = l / 2
        a, b = m / pow(10, lby2), m % pow(10, lby2)
        c , d = n / pow(10, lby2), n % pow(10, lby2)
        p = a + b
        q = c + d
        ac = multiply_optimized(a, c)
        bd = multiply_optimized(b, d)
        adbc = multiply_optimized(p, q) - ac - bd
        res = ac * 10 ** (2 * lby2) + (adbc * 10 ** lby2) + bd
        return  res


def karatsuba(x, y):
    """Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x * y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n / 2

        a = x / 10 ** (nby2)
        b = x % 10 ** (nby2)
        c = y / 10 ** (nby2)
        d = y % 10 ** (nby2)

        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10 ** (2 * nby2) + (ad_plus_bc * 10 ** nby2) + bd

        return prod


print(multiply(5678, 1234))
print(multiply_optimized(5678, 1234))
print(karatsuba(5678, 1234))