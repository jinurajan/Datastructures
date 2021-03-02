"""
Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.



Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:

1 <= n <= 104
"""


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n ** 0.5) + 1)]
        level = 0
        q = {n}
        while q:
            level += 1
            next_queue = set()
            for rem in q:
                for sq in squares:
                    if rem == sq:
                        return level
                    elif rem < sq:
                        break
                    else:
                        next_queue.add(rem - sq)
            q = next_queue
        return level


