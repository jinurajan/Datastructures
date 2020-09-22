"""
    First Missing Positive (Hard)
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

class Solution2(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        1.bring all 0 and -ve values to the left of array
        2. look in the subset of positive array and mark it as -ve 
        3. return i+1 if any of the element is positive after the above iteration
        """
        n = len(nums)
        start_index = 0
        for i in range(n):
            if nums[i] <= 0:
                nums[start_index], nums[i] = nums[i], nums[start_index]
                start_index += 1
        if start_index == n:
            return 1
        size = n - start_index
        return self.find_missing_positive(nums[start_index:], size)

    def find_missing_positive(self, arr, size):
        for i in range(size):
            if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0):
                arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        for i in range(size):
            if arr[i] >= 0:
                return i + 1
        return size + 1


class Solution3(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        1. create hash with number of elements in nums but this could be dangerous if len(nums) are larger
        """

        hash_set = set([nums[i] for i in xrange(len(nums)) if nums[i] > 0])
        i = 1
        while i <= len(hash_set):
            if i not in hash_set:
                return i
            i += 1
        return i


class Solution1(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        1.bring all 0 and -ve values to the left of array
        2. mark rest of the elements in a hash key  
        3. start from 1 and check if it exists in hash else return value

        """
        n = len(nums)
        start_index = 0
        for i in range(n):
            if nums[i] <= 0:
                nums[start_index], nums[i] = nums[i], nums[start_index]
                start_index += 1
        if start_index == n:
            return 1
        return self.find_missing_positive(nums, start_index, n)

    def find_missing_positive(self, arr, start_index, n):
        hash_set = {}
        for i in range(start_index, n):
            hash_set[arr[i]] = 1
        i = 1
        while i < (n - start_index) + 1:
            if i not in hash_set:
                return i
            i += 1
        return i


class Solution(object):
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




print Solution().firstMissingPositive([1,2,0]) == 3
print Solution().firstMissingPositive([3,4,-1,1]) == 2
print Solution().firstMissingPositive([7,8,9,11,12]) == 1
print Solution().firstMissingPositive([1000, -1]) == 1
print Solution().firstMissingPositive([0, 1, 2]) == 3
print Solution().firstMissingPositive([4, 3, 2, 5]) == 1
print Solution().firstMissingPositive([2]) == 1




