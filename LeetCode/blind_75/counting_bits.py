"""
Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Input: n = 2
Output: [0,1,1]

"""
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)

        for x in range(1, n+1):
            dp[x] = dp[x&x-1] + 1
        return dp
    
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)

        for x in range(1, n+1):
            dp[x] = dp[x>>1] + (x&1)
        return dp
    



class Solution:
    def set_bit_count(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
    
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            result.append(self.set_bit_count(i))
        return result
    

class Solution:
    # P(x+b)=P(x)+1,b=2^m >x
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        x = 0
        b = 1
        
        # [0, b) is calculated
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                ans[x + b] = ans[x] + 1
                x += 1
            x = 0 # reset x
            b <<= 1 # b = 2b
            
        return ans      
