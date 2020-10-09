"""
Template #1 is the most basic and elementary form of Binary Search. 
It is the standard Binary Search Template that most high schools or universities use when they first teach students computer science. 
Template #1 is used to search for an element or condition which can be determined by accessing a single index in the array.

Key Attributes:

Most basic and elementary form of Binary Search
Search Condition can be determined without comparing to the element's neighbors (or use specific elements around it)
No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found
 

Distinguishing Syntax:

Initial Condition: left = 0, right = length-1
Termination: left > right
Searching Left: right = mid-1
Searching Right: left = mid+1
"""

class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        return -1


class Solution2(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(nums, l, r, key):
            if l <= r:
                mid = (l + r) / 2
                if nums[mid] == key:
                    return mid
                elif nums[mid] > key:
                    return binary_search(nums, l, mid - 1, key)
                else:
                    return binary_search(nums, mid + 1, r, key)
            return -1
        return binary_search(nums, 0,len(nums)-1, target)


class Solution3(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(nums, l, r, key):
            if l <= r:
                mid = l + (r-l) / 2
                if nums[mid] == key:
                    return mid
                elif nums[mid] > key:
                    return binary_search(nums, l, mid - 1, key)
                else:
                    return binary_search(nums, mid + 1, r, key)
            return -1
        return binary_search(nums, 0, len(nums)-1, target)

print Solution1().search([1,2,3,4,5,6,7], 6)
print Solution2().search([1,2,3,4,5,6,7], 6)
print Solution3().search([1,2,3,4,5,6,7], 6)