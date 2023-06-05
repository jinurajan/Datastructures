"""
Range Sum Query - Mutable

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

"""
from typing import List


class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None
    

class NumArray:
    
    def create_tree(self, array, l, r):
        if l > r:
            return
        if l == r:
            n = Node(l, r)
            n.total = array[l]
            return n
        
        mid = (l + r) // 2
        root = Node(l, r)
        root.left = self.create_tree(array, l, mid)
        root.right = self.create_tree(array, mid+1, r)
        
        root.total = root.left.total + root.right.total
        return root
            

    def __init__(self, nums: List[int]):
        self.root = self.create_tree(nums, 0, len(nums)-1)
    
    def update(self, index: int, val: int) -> None:
        
        def update_val(root, index, val):
            if root.start == root.end:
                root.total = val
                return val
            mid = (root.start + root.end) // 2
            if index <= mid:
                update_val(root.left, index, val)
            else:
                update_val(root.right, index, val)
            root.total = root.left.total +root.right.total
            return root.total
        
        return update_val(self.root, index, val)
    
    def sumRange(self, left: int, right: int) -> int:
        
        def range_sum(root, i, j):
            if root.start == i and root.end == j:
                return root.total
            
            mid = (root.start + root.end) // 2
            if j <= mid:
                return range_sum(root.left, i, j)
            elif i >= mid+1:
                return range_sum(root.right, i, j)
            else:
                return range_sum(root.left, i, mid) + range_sum(root.right, mid+1, j) 
        return range_sum(self.root, left, right)