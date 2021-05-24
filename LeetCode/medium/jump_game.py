"""
Jump Game

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""



class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def backtrack(index):
            if index == n - 1:
                return True
            if index >= n:
                return False
            far_jump = min(index + nums[index], n - 1)
            for i in range(index + 1, far_jump + 1):
                if backtrack(i):
                    return True
            return False

        return backtrack(0)
