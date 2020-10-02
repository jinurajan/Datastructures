"""
Climbing Stairs

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
 

Constraints:

1 <= n <= 45
"""
class Solution(object):
    mem = {0: 0, 1: 1, 2: 2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fib(n):
            if n in self.mem:
                return self.mem[n]
            r = fib(n-1) + fib(n-2)
            self.mem[n] = r
            return r
        if n <= 2:
            return self.mem[n]
        return fib(n)


print(Solution().climbStairs(1))
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))