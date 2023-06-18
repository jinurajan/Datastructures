"""
Additive Number

An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
"""
from typing import List


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        seq = []
        def backtrack(num: str, curr: List[int]):
            if not num:
                return len(curr) >= 3
            
            for i in range(1, len(num)+1):
                if i > 1 and num[0] == '0':
                    break
                if len(curr) < 2 or int(num[:i]) == curr[-1] + curr[-2]:
                    seq.append(int(num[:i]))
                    if backtrack(num[i:], seq):
                        return True
                    seq.remove(int(num[:i]))
            
            return False
        
        return backtrack(num, [])


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i+1, n):
                if num[0] == '0' and i > 1:
                    break
                if num[i] == '0' and j > i+1:
                    break
                
                n1 = int(num[:i])
                n2 = int(num[i:j])

                k = j
                while k < n:
                    n3 = n1 + n2
                    if num[k:].startswith(str(n3)):
                        k += len(str(n3))
                        n1, n2 = n2, n3
                    else:
                        break
                if k == n:
                    return True
        return False
