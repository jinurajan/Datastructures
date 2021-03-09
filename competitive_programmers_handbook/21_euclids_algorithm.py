"""
greatest common divisor of a and b gcd(a, b) is the greatest number that divides both a and b
and the least common multiple of a and b lcm(a, b) is the smallest number that is divisible by both a and b

gcd(24, 36) = 12

lcm(24, 36) = 72

lcm(a, b) = ab / gcd(a, b)


gcd(a, b) = a if b == 0 / gcd(b, a mod b) if b != 0

"""

def gcd(a, b):
    """ complexity = O(logn) """
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(24, 36))
print(gcd(27, 3))
