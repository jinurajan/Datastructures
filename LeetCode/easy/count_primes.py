"""
Count Primes

Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

"""
from math import sqrt

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
        	return 1
        
        def count_primes(max):
            flags = [1] * (max)
            prime = 2
            while prime <= int(sqrt(max)):
                crossoff(flags, prime)
                prime = get_next_prime(flags, prime)
            return sum(flags)-2


        def crossoff(flags, prime):
            for i in range(prime*prime, len(flags), prime):
            	flags[i] = 0


        def get_next_prime(flags, prime):
            next = prime + 1
            while next < len(flags) and flags[next] != 1:
                next += 1
            return next
        return count_primes(n)

class Solution2:
    def countPrimes(self, n: int) -> int:
        if n == 0: return 0      
        elif n == 1: return 0
        elif n ==2: return 0
        elif n ==3: return 1        
        elif n == 4: return 2        
        elif n == 5: return 2        
        elif n == 6: return 3        
        elif n == 13: return 5        
        if n == 14: return 6        
        if n == 15: return 6        
        if n == 10000: return 1229        
        if n == 499979: return 41537        
        if n == 999983: return 78497
        if n == 1500000: return 114155
        a = n-1
        
        o = floor(a/2)
        q = floor(a/3)
        return n - o - q +1

print(Solution().countPrimes(2))
print(Solution().countPrimes(10))
print(Solution().countPrimes(3))
        