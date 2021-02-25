"""
Random Pick Index

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);


"""
import random

from typing import List


class Solution1:

    def __init__(self, nums: List[int]):
        self.ds = defaultdict(lambda: [])
        for idx, n in enumerate(nums):
            self.ds[n].append(idx)

    def pick(self, target: int) -> int:
        result = self.ds[target].pop(0)
        self.ds[target].append(result)
        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class Solution:

    def __init__(self, a: List[int]):
        self.a = a

    def pick(self, t: int) -> int:
        cnt, ans = 0, -1

        for i, e in enumerate(self.a):
            if e != t:
                continue
            cnt += 1
            if random.random() < 1 / cnt:
                ans = i
        return ans