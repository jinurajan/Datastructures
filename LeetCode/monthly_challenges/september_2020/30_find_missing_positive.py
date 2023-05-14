"""
First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
"""
class Solution1(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Uses extra space of n if there are no duplicates and it could be dangerous
        """
        hash_set = set(nums)
        if not hash_set:
            return 1
        for i in range(1,len(hash_set)+1):
            if i not in hash_set:
                return i
        return i + 1


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        nums = [1, 2, 0]

        nums = [1, 2, 0, 0] n = 4

        remove negative elements and element greater than equal to  n as those dont belong here

        loop 1
            i from 0 to 4
            1.1
                i = 0
                nums[1%4] = nums[1] += 4 = [1, 6, 0, 0]
            1.2
                i = 1
                nums[2%4] = nums[2] += 4 = [1, 6, 4, 0]
            1.3
                i = 2
                nums[0 % 4] = nums[0]+= 4 = [5, 6, 4, 0]
            1.4
                i = 3
                nums[0 % 4] = nums[0] += 4 = [9, 6, 4, 0]
        loop 2
            i from 1 to 4
            2.1
                i = 1
                nums[1]/4 = 6 / 4 
            2.2
                i = 2
                nums[2] / 4 = 4 / 4
            2.3
                i = 3
                nums[3]/4 = 0 / 4
                return 3
        """
        nums.append(0)
        n = len(nums)
        for i in range(n): #delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        for i in range(n): #use the index as the hash to record the frequency of each number
            nums[nums[i]%n]+=n
        for i in range(1,n):
            if nums[i]/n==0:
                return i
        return n


class Solution2(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1. create hash with number of elements in nums but this could be dangerous if len(nums) are larger
        """
        n = len(nums)
        start_index = 0
        for i in range(n):
            if nums[i] <= 0:
                nums[start_index], nums[i] = nums[i], nums[start_index]
                start_index += 1
        if start_index == n:
            return 1
        hash_set = set([nums[i] for i in xrange(start_index, len(nums))])
        i = 1
        while i <= len(hash_set):
            if i not in hash_set:
                return i
            i += 1
        return i




print Solution().firstMissingPositive([1,2,0])
print Solution().firstMissingPositive([3,4,-1,1])
print Solution().firstMissingPositive([7,8,9,11,12])
