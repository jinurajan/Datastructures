"""
Sqrt(x)

Solution
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.


4 -> 2, 2 return 2

8 -> 4 

8 -> 4 -> 2 -> 1

"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        sq_rt = 0
        def binary_find(l, r, x, sq_rt):
            if l <= r:
                mid = (l + r) / 2
                cal_sq = mid * mid
                if cal_sq <= x and sq_rt < mid:
                    sq_rt = mid
                if cal_sq > x:
                    return binary_find(l, mid - 1, x, sq_rt)
                return binary_find(mid + 1, r, x, sq_rt)
            return sq_rt
        return binary_find(0, x-1, x, sq_rt)




print Solution().mySqrt(8)
print Solution().mySqrt(4)
print Solution().mySqrt(6)
print Solution().mySqrt(0)
print Solution().mySqrt(1)
print Solution().mySqrt(2)
print Solution().mySqrt(3)