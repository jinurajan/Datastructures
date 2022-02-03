"""
454. 4Sum II

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""

from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        mem = Counter()
        for a in nums1:
            for b in nums2:
                mem[a+b] += 1
        for c in nums3:
            for d in nums4:
                count += mem[-(c+d)]
        return count


from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        m = Counter()
        def num_count(lists: List[List[int]]) -> int:
            add_to_hash(lists, 0, 0)
            return count_complements(lists, len(lists)//2, 0)
        
        def add_to_hash(lists: List[List[int]], i:int, sum:int) -> None:
            if i == len(lists) // 2:
                m[sum] += 1
            else:
                for a in lists[i]:
                    add_to_hash(lists, i+1, sum+a)
        
        
        def count_complements(lists: List[List[int]], i:int, complement: int) -> int:
            if i == len(lists):
                return m.get(complement, 0)
            count = 0
            for a in lists[i]:
                count += count_complements(lists, i+1, complement-a)
            return count
        return num_count([nums1, nums2, nums3, nums4])
        