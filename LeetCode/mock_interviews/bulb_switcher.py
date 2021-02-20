"""
Bulb Switcher

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb is on.

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1

Constraints:

0 <= n <= 109
"""
from math import sqrt

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))

class Solution1:
    def bulbSwitch(self, n: int) -> int:
        on_bulbs = 0
        for bulb in range(1, n+1):
            factors = 0
            for row in range(1, int(pow(n, 0.5))+1):
                if bulb % row == 0:
                    factors += 1
                    if bulb // row != row:
                        factors += 1
            if factors % 2 == 1:
                on_bulbs += 1
        return  on_bulbs

print(Solution().bulbSwitch(0))
print(Solution().bulbSwitch(1))
print(Solution().bulbSwitch(2))
print(Solution().bulbSwitch(3))
print(Solution().bulbSwitch(4))
print(Solution().bulbSwitch(5))
print(Solution().bulbSwitch(6))
print(Solution().bulbSwitch(7))
print(Solution().bulbSwitch(8))
print(Solution().bulbSwitch(9))
print(Solution().bulbSwitch(10))


