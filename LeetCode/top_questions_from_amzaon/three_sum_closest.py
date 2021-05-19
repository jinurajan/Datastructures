"""
 3Sum Closest

 Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


Constraints:

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float("inf")
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                sum_val = nums[i] + nums[l] + nums[r]
                if abs(target - sum_val) < abs(diff):
                    diff = target - sum_val
                if sum_val > target:
                    r -= 1
                else:
                    l += 1
                if diff == 0:
                    # found matching one
                    break
        return target - diff



class Solution1:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float("inf")
        for i in range(n):
            for j in range(i+1, n):
                compliment = target - nums[i] - nums[j]
                hi = bisect_right(nums, compliment, j+1)
                lo = hi - 1
                if hi < n and abs(compliment - nums[hi]) < abs(diff):
                    diff = compliment - nums[hi]
                if lo > j and abs(compliment - nums[lo]) < abs(diff):
                    diff = compliment - nums[lo]
                if diff == 0:
                    break
        return target - diff

