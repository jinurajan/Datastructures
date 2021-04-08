"""
Permutation Sequence

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.



Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"


Constraints:

1 <= n <= 9
1 <= k <= n!

"""

from math import factorial, ceil


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i + 1 for i in range(n)]
        result = []
        def search(first, rem, nums):
            if rem == 0 and first == n:
                result = nums[:]
                return
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                search(first + 1, rem - 1, nums)
                nums[first], nums[i] = nums[i], nums[first]
            return

        each_set_count = factorial(n - 1)
        start_idx = ceil(k / each_set_count) - 1
        rem = k % each_set_count
        import pdb;
        pdb.set_trace()
        search(start_idx, rem, nums)
        return result


print(Solution().getPermutation(4, 16))



