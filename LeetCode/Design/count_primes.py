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


Constraints:

0 <= n <= 5 * 106
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [0 for i in range(n)]
        for i in range(2, n):
            if sieve[i]:
                continue
            for j in range(2 * i, n, i):
                sieve[j] = i
        return sum([1 for i in range(2, n) if sieve[i] == 0])
