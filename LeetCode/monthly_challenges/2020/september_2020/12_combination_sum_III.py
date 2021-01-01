"""
216. Combination Sum III
Medium
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        if k == 0 or n == 0 or n > 45:
            return result
        max_val = min(9, n)
        def dfs(no, start_num, curr_val, curr_sum):
            if curr_sum == n and k == no:
                # found one combination
                result.append(curr_val[:])
            elif no > k or curr_sum > n:
                # crossed k values or current sum 
                return
            else:
                for i in range(start_num+1, 10):
                    curr_val.append(i)
                    dfs(no+1, i, curr_val, curr_sum+i)
                    # if returns means invalid
                    curr_val.pop()
        dfs(0, 0, [], 0)
        return result



class Solution1(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        def dfs(i, arr):
            if len(arr) == k and sum(arr) == n:
                result.append(arr)
                return
            elif len(arr) >= k:
                return
            for j in range(i, 10):
                dfs(j+1, arr+[j])
        dfs(1, [])
        return result



print Solution().combinationSum3(3, 9)
print Solution().combinationSum3(3, 7)

print "***********"
print Solution1().combinationSum3(3, 9)
print Solution1().combinationSum3(3, 7)
