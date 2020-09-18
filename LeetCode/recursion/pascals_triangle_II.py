"""
Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 40
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        loop 1
        	C = 1
        	result = [1]
        	C = 1 * (4-1) / 1 = 3
        loop 2
        	result = [1, 3]
        	C = 3 * (4-2)/ 2 = 3 * 2 / 2 = 3

        loop 3
        	result = [1, 3, 3]
        	C = 3 * (4 - 3) / 3 = 1

        loop 4
        	result = [1, 3, 3, 1]
        	C = 1 * (4-4) / 4 = 0
        """
        result = []
        C = 1
        rowIndex += 1
    	for i in range(1, rowIndex + 1):
    		result.append(C)
    		C = int(C * (rowIndex-i)/ i)
        return result




class Solution1(object):
    
    def nextf(self, v, k, n):
        return v * (n-k) // (k+1) 
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
		
		l  = [1, 1, 1, 1, 1] (row_index + 1) length
		mid = 3

		first loop: fill the first half of l
			k = 1
				l[k-1] = 1
				k - 1 = 0
				n = 4
				l[k] = 1 * 4 - 0 // 2 = 4 l = [1, 4, 1, 1, 1]
			k = 2
				l[k-1] = 4
				k - 1 = 1
				n = 4
				l[k] = 4 * (4-1) // 2 = 2 * 3 = 6 l = [1, 4, 6, 1, 1]
		fill the second half using first half
			k = 3 
				l[3] = l[4-3] = l[1] = 4 [1, 4, 6, 4, 1]
        """
        n = rowIndex
        l = [1] * (n + 1)
        mid = n // 2 + 1
        for k in range(1, mid):
            l[k] = self.nextf(l[k-1], k-1, n)
        for k in range(mid, n):
            l[k] = l[n - k]
        return l
		

print Solution().getRow(0)
print Solution().getRow(1)
print Solution().getRow(2) 
print Solution().getRow(3)
print Solution().getRow(4)
print Solution().getRow(5)
print Solution().getRow(6)


print Solution1().getRow(0)
print Solution1().getRow(1)
print Solution1().getRow(2)
print Solution1().getRow(3)
print Solution1().getRow(4)
print Solution1().getRow(5)
print Solution1().getRow(6)
