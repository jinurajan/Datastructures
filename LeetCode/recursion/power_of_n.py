"""
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
"""
class Solution3(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        Does not work for bigger numbers
        """
        flag = 0
        if n < 0:
            flag = 1
            n = -1 * n

        def pow(x, n, ans, flag):
            if n == 0:
                return ans
            if flag:
                return pow(x, n-1, ans * (1/float(x)), flag)
            else:
                return pow(x, n-1, ans * x, flag)

        return pow(x, n, 1, flag)



class Solution4(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        Only works for n > 0 and x > 0
        """
        if n == 0:
            return 1
        t = self.myPow(x, int(n/2))
        if n % 2 == 0:
            return t * t
        if n > 0:
            return (x * t * t)
        else:
            return (t * t) / x

class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res, positive = 1, True
        if x == 0:
            return 0
        if n == 0:
            return 1
        elif n < 0:
            n *= -1
            positive = None
        while n != 0:
            if n % 2 == 1:
                res *= float(x)
            n = n // 2
            x *= float(x)
        if positive:
            return res
        else:
            return 1 / res


class Solution1(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            n = -n
            x = 1/float(x)

        def power(x, n):
            if n == 0:
                return 1
            if n == 1:
                return float(x)
            return power(float(x), n/2) * power(float(x), n/2)
        if n % 2 == 0:
            return power(x, n/2) * power(x, n/2)
        else:
            return x * power(x, n/2) * power(x, n/2)

class Solution(object):
    mem = {}
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        pos = 1
        if n < 0:
            pos = -1
            n = -n
            x = 1/float(x)

        def power(x, n):
            if n == 0:
                return 1
            if n in self.mem:
                return self.mem[n]
            result = self.myPow(x, n//2) * self.myPow(x, n//2)
            if n % 2 == 1:
                result *= pos * float(x)
            self.mem[n] = result
        return power(float(x), n)



print Solution().myPow(2, 0)
print Solution().myPow(2, 1)
print Solution().myPow(2, 2)
print Solution().myPow(2, 3)
print Solution().myPow(2, 4)
print Solution().myPow(2, 5)
print Solution().myPow(2, -2)

print Solution().myPow(0.00001, 2147483647)
print Solution().myPow(2.10000, 3)
