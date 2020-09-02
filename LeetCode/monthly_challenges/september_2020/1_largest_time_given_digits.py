"""
Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
 

Note:

A.length == 4
0 <= A[i] <= 9
"""


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        hash_map = {}
        for each in A:
            if each in hash_map:
                hash_map[each] += 1
            else:
                hash_map[each] = 1
        # import pdb; pdb.set_trace()
        no_gt_5 = self.check_gt_5_numbers(hash_map)
        if no_gt_5 > 2:
            # we can have only 2 one in 2nd H and one in 2nd M in HH:MM format. 
            return ""
        # print no_gt_5
        if no_gt_5 > 1:
            # HH should have one of the greater number
            a = self.dfs(hash_map, 1)
            if a is None:
                return ""
            b = self.dfs(hash_map, 9)
            if b is None:
                return ""
            c = self.dfs(hash_map, 5)
            if c is None:
                return ""
            d = self.dfs(hash_map, 9)
            if d is None:
                return ""
        else:
            a = self.dfs(hash_map, 2)
            if a is None:
                return ""
            if a == 2:
                b = self.dfs(hash_map, 3)
            else:
                b = self.dfs(hash_map, 9)
            if b is None:
                return ""
            c = self.dfs(hash_map, 5)
            if c is None:
                return ""
            d = self.dfs(hash_map, 9)
            if d is None:
                return ""
        return "{}{}:{}{}".format(a, b, c, d)

    def check_gt_5_numbers(self, hash_map):
        c = 0
        for key in hash_map:
            if key > 5:
                c += hash_map[key]
        return c

    def dfs(self, hash_map, val):
        r = None
        while val >= 0:
            if val in hash_map:
                r = val
                hash_map[val] -= 1
                if hash_map[val] == 0:
                    del hash_map[val]
                break
            else:
                val -= 1
        return r


print Solution().largestTimeFromDigits([1, 2, 3, 4]) == "23:41"
print Solution().largestTimeFromDigits([5, 5, 5, 5]) == ""
print Solution().largestTimeFromDigits([0, 0, 0, 0]) == "00:00"
print Solution().largestTimeFromDigits([0, 4, 0, 0]) == "04:00"
print Solution().largestTimeFromDigits([2, 0, 6, 6]) == "06:26"
