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
from math import floor, sqrt

class Solution4(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        NOTE: this does not work for bigger numbers
        as approximation can give little difference
        """
        if n < 1:
            return n
        gr = 1.6180339
        return int(floor((pow(gr, n+1) - pow((1-gr), n+1)) / sqrt(5)))


mem = {0: 0, 1: 1}

def fibonacci_using_memoization(n):
    if n in mem:
        return mem[n]

    result = fibonacci_using_memoization(n-1) + \
            fibonacci_using_memoization(n-2)
    mem[n] = result
    return result


class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return fibonacci_using_memoization(n+1)




mem_1 = {1:1, 2: 2}

class Solution3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in mem_1:
            return mem_1[n]
        result = self.climbStairs(n-1) + self.climbStairs(n-2)
        mem_1[n] = result
        return result

class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        first, second = 1, 2
        for i in range(3, n+1):
            first, second = second, first + second
        return second


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        # using constant 2 values before
        loop 1
            fib_n = [1, 2]
        loop 2 
            fib_n = [2, 3]

        loop 3
            fib_n = [3, 5]

        loop 5
            fib_n = [5, 8]
        and so on 
        """
        if n <= 2:
            return n
        fib_n = [1, 2]
        for i in range(3, n+1):
            fib_n = [fib_n[1], sum(fib_n)]
        return fib_n[1]






# print Solution().climbStairs(2)
# print Solution().climbStairs(3)
# print Solution().climbStairs(4)
# print Solution().climbStairs(5)

# print Solution1().climbStairs(2)
# print Solution1().climbStairs(3)
# print Solution1().climbStairs(4)
# print Solution1().climbStairs(5)

print Solution().climbStairs(35)
print Solution1().climbStairs(35)
print Solution2().climbStairs(35)
print Solution3().climbStairs(35)
print Solution4().climbStairs(35)
