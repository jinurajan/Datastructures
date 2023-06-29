"""
Expression Add Operators

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Thoughts
1. require checking * hence store the previous value 

"""
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        def dfs(candidate, idx, total, prev):
            if idx == len(num) and total == target:
                result.append(candidate)
                return
            for j in range(idx+1, len(num)+1):
                s = num[idx:j]
                d = int(s)
                if num[idx] == '0' and s != '0':
                    continue
                if not candidate:
                    dfs(s, j, d, d)
                else:
                    dfs(candidate+ '+' + s, j, total+d, d)
                    dfs(candidate+ '-' + s, j, total-d, -d)
                    dfs(candidate+ '*' + s, j, total-prev+prev*d, prev*d)
        
        dfs('', 0, 0,0)
        return result
