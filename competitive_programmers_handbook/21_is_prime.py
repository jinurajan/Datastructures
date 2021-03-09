"""
Check if a given number is prime
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(pow(n, 0.5))):
        if n % i == 0:
            return False
    return True

def factors(n):
    result = []
    for i in range(2, int(pow(n, 0.5))):
        if n % i == 0:
            result.append(i)
            n /= i
    if n > 1:
        result.append(n)
    return result

def sieve_of_eratosthenes(n):
    """ Preprocessing Algorithm to check if a given number between 2
    and n is a prime if not find one prime factor of the number
    Time complexity = O(nlogn)
    """
    sieve = [0 for i in range(n+1)]
    for i in range(2, n+1):
        if sieve[i]:
            continue
        for j in range(2*i, n+1, i):
            sieve[j] = i
    return sieve


print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(5))
print(is_prime(7))
print(is_prime(14))
print(is_prime(11))


print(factors(1))
print(factors(2))
print(factors(3))
print(factors(4))
print(factors(5))
print(factors(7))
print(factors(14))
print(factors(11))

result = sieve_of_eratosthenes(20)
for idx, n in enumerate(result):
    if n == 0:
        print(idx, 'is prime')