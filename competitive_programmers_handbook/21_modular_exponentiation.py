"""
x raised to n mod m
"""

def modpow(x, n, m):
    if n == 0:
        return 1 % m
    u = modpow(x, n//2, m)
    u = (u*u) % m
    if n %2 == 1:
        u = (u*x) % m
    return u

print(modpow(2, 10, 5))