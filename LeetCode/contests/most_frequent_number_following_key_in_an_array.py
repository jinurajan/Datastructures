






from typing import List

from collections import Counter
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counter = Counter()
        prev = None
        for num in nums:
            if prev and prev == key:
                counter[num] += 1
            prev = num
        return max(counter, key=counter.get)

nums = [1,100,200,1,100]
key = 1
print(Solution().mostFrequent(nums=nums, key=key))
nums = [2,2,2,2,3]
key = 2
print(Solution().mostFrequent(nums=nums, key=key))