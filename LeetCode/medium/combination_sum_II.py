"""
Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
 Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List

class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        values = []
        visited = set()
        def backtrack(index, sum_1, sum_2):
            if sum_1 == target or sum_2 == target:
                if tuple(sorted(values)) not in visited:
                    result.append(sorted(values[:]))
                visited.add(tuple(sorted(values)))
                return
            elif index == n:
                return
            values.append(candidates[index])
            backtrack(index+1, sum_1+candidates[index], sum_2-candidates[index])
            values.pop()
            backtrack(index+1, sum_1, sum_2 - candidates[index])
        backtrack(0, 0, sum(candidates))
        return sorted(result)

class Solution1:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        values = []
        visited = set()
        def backtrack(index, sum_1, sum_2):
            if sum_1 == target or sum_2 == target:
                if tuple(sorted(values)) not in visited:
                    result.append(sorted(values[:]))
                visited.add(tuple(sorted(values)))
                return
            if index == n:
                return
            values.append(candidates[index])
            backtrack(index+1, sum_1+candidates[index], sum_2 - candidates[index])
            values.pop()
            backtrack(index + 1, sum_1, sum_2 - candidates[index])
        backtrack(0, 0, sum(candidates))
        return sorted(result)


from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(combination, balance, current, counter, results):
            if balance == 0:
                result.append(list(combination))
                return
            elif balance < 0:
                return
            for next_curr in range(current, len(counter)):
                candidate, freq = counter[next_curr]
                if freq <= 0:
                    continue
                combination.append(candidate)
                counter[next_curr] = (candidate, freq-1)
                backtrack(combination, balance-candidate, next_curr, counter, results)
                counter[next_curr] = (candidate, freq)
                combination.pop()
        result = []
        counter = Counter(candidates)
        counter = [(c, counter[c]) for c in counter]
        backtrack([], target, 0, counter, result)
        return result


candidates = [10,1,2,7,6,1,5]
target = 8
print(Solution().combinationSum2(candidates, target))
candidates = [2,5,2,1,2]
target = 5
print(Solution().combinationSum2(candidates, target))
