"""
Given an array of integers, nums, find a duplicate number such that the array contains 
�
+
1
n+1
 elements, and each integer is in the range 
[
1
,
�
]
[1,n]
 inclusive.

There is only one repeated number in nums. Find and return that number.

Note: You cannot modify the given array nums. You have to solve the problem using only constant extra space.
"""

def find_duplicate(nums):
    n = len(nums)
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast

