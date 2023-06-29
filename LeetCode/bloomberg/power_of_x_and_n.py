"""
Pow(x, n)


Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        mem = {1: x}
        
        def power(x,n):
            if n == 0:
                return 1
            if n in mem:
                return mem[n]
            
            result = power(x, n//2) * power(x, n//2)
            
            if n % 2 == 1:
                result *= power(x, 1)
            mem[n] = result
            return result
        
        result = power(x, abs(n))
        if n < 0:
            return 1/ result
        return result
        