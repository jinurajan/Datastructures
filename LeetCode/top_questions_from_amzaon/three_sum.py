"""

"""
from typing import List
from collections import defaultdict
from bisect import bisect_left

from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3 or min(nums) > 0 or max(nums) < 0:
            return []
        res = []
        count = Counter(nums)
        nums = sorted(count)
        print(nums)
        for idx, num in enumerate(nums):
            if num > 0:
                break
            two_sum = - num
            num2_min, num2_max = two_sum - nums[-1], two_sum / 2
            i = bisect_left(nums, num2_min, idx + 1)
            j = bisect_left(nums, num2_max, i)
            for num2 in nums[i:j]:
                num3 = two_sum - num2
                if num3 in count:
                    res.append((num, num2, num3))
        for num in nums:
            if count[num] > 1:
                if num == 0 and count[num] >= 3:
                    res.append((num, num, num))
                elif num != 0 and 0 - 2 * num in count:
                    res.append((num, num, 0 - 2 * num))
        return res


class Solution1:
    def two_sum(self, nums, right, target):
        left = 0
        results = []
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                results.append([nums[left], nums[right]])
            if s < target:
                left += 1
            else:
                right -= 1
        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        visited = set()
        n = len(nums)
        for i in range(n-1, 1, -1):
            two_sums = self.two_sum(nums, i-1, -nums[i])
            for two_sum in two_sums:
                r = two_sum +[nums[i]]
                if tuple(r) not in visited:
                    results.append(r)
                    visited.add(tuple(r))
        return results


nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))