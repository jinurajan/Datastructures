"""
Given the two distinct integer arrays, nums1 and nums2, where nums1 is a subset of nums2, find all the next greater elements for nums1 values in the corresponding places of nums2.


1. nums1 is a subset of nums2
2. 
"""

def next_greater_element(nums1, nums2):
    stack = []
    map = {}
    "create a map where key is current value and value is next greater element"
    for current in nums2:
        while stack and current > stack[-1]:
            map[stack.pop()] = current
        stack.append(current)
    # if stack is not empty it has the highest number set the next greater value as -1
    while stack:
        map[stack.pop()] = -1
    result = []
    for num in nums1:
        result.append(map[num])
    return result



print(next_greater_element([2,4], [1,2,3,4]))