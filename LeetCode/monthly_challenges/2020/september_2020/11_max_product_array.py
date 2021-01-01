"""
152. Maximum Product Subarray medium

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

class Solution1(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reverse = nums[::-1]
        
        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] or 1
            reverse[i] *= reverse[i-1] or 1
        
        return max(nums+reverse)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            # more than one element
            left_most_negative = None
            max_pdt = nums[0]
            running_pdt = 1
            for n in nums:
                if not n:
                    # means n is 0
                    left_most_negative = None
                    max_pdt = max(max_pdt, n)
                    running_pdt = 1
                    continue
                else:
                    # for any other numbers other than zero
                    running_pdt *= n
                    if running_pdt < 0:
                        if not left_most_negative:
                            # no negative numbers
                            left_most_negative = running_pdt
                        else:
                            max_pdt = max(max_pdt, running_pdt // left_most_negative)
                    else:
                        # positive number
                        max_pdt = max(max_pdt, running_pdt)
        return max_pdt


print Solution().maxProduct([1]) == 1
print Solution().maxProduct([-2]) == -2
print Solution().maxProduct([-3, -1, -1]) == 3
print Solution().maxProduct([2, 3, -2, 4]) == 6
print Solution().maxProduct([2, 3, -2, 4, 5]) == 20
print Solution().maxProduct([-2, 0, -1]) == 0
print Solution().maxProduct([0, 2]) == 2
print Solution().maxProduct([7, -2, -4]) == 56
print Solution().maxProduct([-2,3,-4]) == 24
print Solution().maxProduct([6,3,-10,0,2]) == 18

print "*********************"


print Solution1().maxProduct([1]) == 1
print Solution1().maxProduct([-2]) == -2
print Solution1().maxProduct([-3, -1, -1]) == 3
print Solution1().maxProduct([2, 3, -2, 4]) == 6
print Solution1().maxProduct([2, 3, -2, 4, 5]) == 20
print Solution1().maxProduct([-2, 0, -1]) == 0
print Solution1().maxProduct([0, 2]) == 2
print Solution1().maxProduct([7, -2, -4]) == 56
print Solution1().maxProduct([-2,3,-4]) == 24
print Solution1().maxProduct([6,3,-10,0,2]) == 18
