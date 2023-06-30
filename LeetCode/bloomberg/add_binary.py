"""
Add Binary

Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101"

"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        n = max(len(a), len(b))
        a,b = a.zfill(n), b.zfill(n)
        carry = 0
        for i in range(n-1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1
            if carry % 2 == 1:
                result += "1"
            else:
                result += "0"
            carry //= 2
        if carry == 1:
            result += "1"
        return result[::-1]
        

        

            
