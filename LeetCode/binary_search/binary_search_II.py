"""
Template #2 is an advanced form of Binary Search. 
It is used to search for an element or condition which requires accessing 
the current index and its immediate right neighbor's index in the array.

Key Attributes:

An advanced way to implement Binary Search.
Search Condition needs to access element's immediate right neighbor
Use element's right neighbor to determine if condition is met and decide whether to go left or right
Gurantees Search Space is at least 2 in size at each step
Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.
 

Distinguishing Syntax:

Initial Condition: left = 0, right = length
Termination: left == right
Searching Left: right = mid
Searching Right: left = mid+1
"""

def binary_search(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums) -1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    if l != len(nums) and nums[l] == target:
        return l
    return -1



def binarySearch1(nums, target):
    if len(nums) == 0:
        return -1

    def bin_search(nums, l, r, target):
        if l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                return bin_search(nums, l, mid, target)
            else:
                return bin_search(nums, mid+1, r, target)
        return l


    l = bin_search(nums, 0, len(nums)-1, target)
    if nums[l] == target:
        return l
    if l - 1 < len(nums) and nums[l-1] == target:
        return l - 1
    return -1


print(binary_search([1, 2, 3, 4, 5, 7], 7))
print(binary_search([1, 2, 3, 4, 5, 7], 1))
print(binarySearch1([1, 2, 3, 4, 5, 7], 4))
print(binary_search([1, 2, 3, 4, 5, 7], 6))

print("***********")
print(binarySearch1([1, 2, 3, 4, 5, 7], 7))
print(binarySearch1([1, 2, 3, 4, 5, 7], 1))
print(binarySearch1([1, 2, 3, 4, 5, 7], 4))
print(binarySearch1([1, 2, 3, 4, 5, 7], 6))