"""
Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for line in range(1, numRows+1):
            l = []
            C = 1
            for j in range(1,line+1):
                l.append(C)
                C = int(C* (line-j)/j)
            result.append(l)
        return result
        

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        result = [[1]]

        for i in range(1, numRows):
            curr_row = []
            prev_row = result[i-1]
            curr_row.append(1)
            for col in range(1, len(prev_row)):
                curr_row.append(prev_row[col-1]+prev_row[col])
            curr_row.append(1)
            result.append(curr_row)
        return result
