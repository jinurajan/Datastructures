
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        min_sum = 0
        if not cost:
            return min_sum
        cost = sorted(cost, reverse=True)
        while cost:
            if len(cost) < 2:
                break
            x1 = cost.pop(0)
            x2 = cost.pop(0)
            min_sum += x1 + x2
            if not cost:
                break
            cost.pop(0)
        if cost:
            min_sum += sum(cost)
        return min_sum
            

cost = [1, 2, 3]
print(Solution().minimumCost(cost))

cost = [5, 5]
print(Solution().minimumCost(cost))

cost = [6,5,7,9,2,2]
print(Solution().minimumCost(cost))