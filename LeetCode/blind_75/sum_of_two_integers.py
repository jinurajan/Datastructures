"""
Sum of Two Integers

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Input: a = 1, b = 2
Output: 3

1. use bit operations xor and find the carry to sum up
2. use bit operation xor and get the borrow to find the difference 

x = 15  0 1 1 1 1
y = 2   0 0 0 1 0

x^ y =  0 1 1 0 1 -> dont have the carry from 1 + 1

(x&y) << 1 - 0 0 1 0 0 -> this has the carry of 1 at possition 


difference between two numbers

x = 15  0 1 1 1 1
y = 2   0 0 0 1 0

x ^ y = 0 1 1 0 1 (no borrow of 1 -1)

(~x & y ) << 1 

~x 1 0 0 0 0
 y 0 0 0 1 0
 -----------
   0 0 0 0 0 << 1 -> 0 0 0 0 0  

"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # 11111111 11111111 11111111 11111111 - 32 bits
        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF # 0111111 11111111 11111111 11111111 31 bites
        return a if a < max_int else ~(a ^ mask)


class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)
        
        # abs(a) >= abs(b) --> 
        # a determines the sign
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow
        
        return x * sign
    

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure x >= y
        if x < y:
            return self.getSum(b, a)  
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        
        return x * sign