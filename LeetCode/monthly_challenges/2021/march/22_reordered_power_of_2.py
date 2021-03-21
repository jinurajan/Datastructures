"""
Reordered Power of 2
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true


Note:

1 <= N <= 10^9

"""

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        a = 1
        N = sorted(str(N))
        while len(str(a)) < len(N):
            a *= 2
        while len(str(a)) == len(N):
            b = sorted(str(a))
            if b == N:
                return True
            a *= 2
        return False


from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        for p in permutations(str(N)):
            string = "".join(p)
            if string.startswith('0'):
                continue
            val = int(string)
            if not val & val - 1:
                return True
        return False

