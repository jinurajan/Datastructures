"""
665. Non-decreasing Array (Easy)
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 

Constraints:

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
        	# only element
        	return True
        peak_element_count = 0
        peak_element = -1
        n = len(nums)
        for i in range(0, len(nums)):
        	if i == 0:
        		peak_element = nums[0] if (nums[i+1] < nums[0] and nums[i+1] > peak_element) else peak_element
        		peak_element_count += 1
        	elif i == n - 1:
        		peak_element = nums[n-1] if (nums[i-1] < nums[n-1] and nums[i] > peak_element) else peak_element
        	else:
        		prev = 0 if i-1 < 0 else nums[i-1]
        		next = 0 if i+1 > n - 1 else nums[i+1]
        		if nums[i] > prev and nums[i] > next:
        			peak_element = nums[i] if nums[i] > peak_element else peak_element
        			peak_element_count += 1
        # print peak_element_count , peak_element
        return True if peak_element_count <= 1 else False



print Solution().checkPossibility([4,2,3]) == True
print Solution().checkPossibility([4,2,1]) == False
print Solution().checkPossibility([2, 3, 4]) == True
print Solution().checkPossibility([2, 4, 3]) == True
print Solution().checkPossibility([2]) == True
print Solution().checkPossibility([3, 4, 2, 3]) == False
