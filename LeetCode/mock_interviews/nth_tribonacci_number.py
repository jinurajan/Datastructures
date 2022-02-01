"""
N-th Tribonacci Number

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.



Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537

Constraints:

0 <= n <= 37
The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

"""

mem_map = {0:0, 1:1, 2:1}
class Solution:
    def tribonacci(self, n: int) -> int:
        if n in mem_map:
            return mem_map[n]
        trib_n = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        mem_map[n] = trib_n
        return trib_n


class Solution:
    def __init__(self):
        self.mem_map = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in self.mem_map:
            return self.mem_map[n]
        self.mem_map[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return self.mem_map[n]


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0

        x, y, z = 0, 1, 1
        for _ in range(n - 2):
            x, y, z = y, z, x + y + z
        return z

