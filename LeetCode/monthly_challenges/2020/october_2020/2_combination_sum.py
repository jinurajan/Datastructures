"""
Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500


1. when target becomes zero means - found a combination return
2. when target becomes less than zero - return no combination
3. there could be multiple combinations starting from same index. take care of it

"""

from typing import List

class Solution1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb_sum(idx, curr, comb, res):
            if curr > target:
                return
            if curr == target:
                res.append(comb)
                return
            for j in range(idx, len(candidates)):
                comb_sum(j, curr + candidates[j], comb + [candidates[j]], res)

        res = []
        comb_sum(0, 0, [], res)
        return res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        using dynamic programming
        candidates = [2,3,5] , 8

        dp = [[], [], [], [], [], [], [], [], []]
        2
        [[], [], [[2]], [], [], [], [], [], []]
        [[], [], [[2]], [], [[2, 2]], [], [], [], []]
        [[], [], [[2]], [], [[2, 2]], [], [[2, 2, 2]], [], []]
        3
        [[], [], [[2]], [[3]], [[2, 2]], [], [[2, 2, 2]], [], [[2, 2, 2, 2]]]
        [[], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2]], [], [[2, 2, 2, 2]]]
        [[], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2], [3, 3]], [], [[2, 2, 2, 2]]]
        [[], [], [[2]], [[3]], [[2, 2]], [[2, 3]], [[2, 2, 2], [3, 3]], [[2, 2, 3]], [[2, 2, 2, 2]]]
        5
        [[], [], [[2]], [[3]], [[2, 2]], [[2, 3], [5]], [[2, 2, 2], [3, 3]], [[2, 2, 3]], [[2, 2, 2, 2], [2, 3, 3]]]
        [[], [], [[2]], [[3]], [[2, 2]], [[2, 3], [5]], [[2, 2, 2], [3, 3]], [[2, 2, 3], [2, 5]], [[2, 2, 2, 2], [2, 3, 3]]]

        """
        dp = [[] for _ in range(target+1)]
        import pdb; pdb.set_trace()
        for c in candidates:
            print(c)           
            for i in range(1, target+1):
                if i < c :
                    continue
                if i == c:
                    dp[i].append([c])
                else:
                    print(i-c, dp[i-c])
                    for blist in dp[i-c]:
                        print(dp)
                        dp[i].append(blist+[c])
                            
        return dp[target]




# print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))

        