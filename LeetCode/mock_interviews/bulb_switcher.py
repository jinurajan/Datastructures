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


class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        array = [1 for i in range(n)]
        print(array)
        for i in range(2, n+1):
            for j in range(1, len(array)):
                if j % i == 1:
                    print(j, i)
                    array[j] ^= 1
            print(array)
        return sum(array)

# print(Solution().bulbSwitch(0))
# print(Solution().bulbSwitch(1))
# print(Solution().bulbSwitch(2))
print(Solution().bulbSwitch(3))
# print(Solution().bulbSwitch(4))
# print(Solution().bulbSwitch(5))
# print(Solution().bulbSwitch(6))


