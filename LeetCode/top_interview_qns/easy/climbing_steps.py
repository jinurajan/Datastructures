"""
climbing Stairs

Solution
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

MEM_MAP = {0:0, 1:1, 2:2}

class SolutionRecursion(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        Uses more memory space than iteration
        """
        if n in MEM_MAP:
            return MEM_MAP[n]
        else:
            MEM_MAP[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return MEM_MAP[n]


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in MEM_MAP:
            return MEM_MAP[n]
        for i in range(3, n + 1):
            MEM_MAP[i] = MEM_MAP[i - 1] + MEM_MAP[i - 2]
        return MEM_MAP[n]


if __name__ == "__main__":
    print SolutionRecursion().climbStairs(1)
    print SolutionRecursion().climbStairs(2)
    print SolutionRecursion().climbStairs(3)
    print SolutionRecursion().climbStairs(4)
    print SolutionRecursion().climbStairs(5)
    print ""
    print Solution().climbStairs(1)
    print Solution().climbStairs(2)
    print Solution().climbStairs(3)
    print Solution().climbStairs(4)
    print Solution().climbStairs(5)
