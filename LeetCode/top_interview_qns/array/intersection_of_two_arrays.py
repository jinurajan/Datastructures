"""
Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""
from typing import List

class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        if not nums1 or not nums2:
            return []
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == n2:
            s = nums1 if nums1[-1] < nums2[-1] else nums2
        else:
            s = nums1 if len(nums1) < len(nums2) else nums2
        b = nums2 if s is nums1 else nums2
        l = 0
        r = len(b) - 1
        sl = 0
        sr = len(s) -1
        if sr == 0:
            # small array is only single element
            return [s[sl]]
        while l < r:
            if b[l] <= s[sl] and b[r] <= s[sr]:
                return [b[l], b[r]]
            if b[l] < s[sl]:
                l += 1
            if b[r] > s[sr]:
                r -= 1
        if l == r:
            return [b[l]]

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        B=[]
        import pdb; pdb.set_trace()
        for i in nums1:
            if i in nums2:
                B.append(i)
                nums2.remove(i)
        return B

# print(Solution().intersect([1,2,2,1], [2,2]))
# print(Solution().intersect([4,9,5], [9,4,9,8,4]))
# print(Solution().intersect([], []))
# print(Solution().intersect([1], [1]))
# print(Solution().intersect([1], [1, 1]))
print(Solution().intersect([1, 2], [1, 1]))
