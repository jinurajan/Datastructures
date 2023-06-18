"""
Two City Scheduling

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        difference = sorted([(a-b, a, b) for a, b in costs])
        total_diff = len(difference)
        for i in range(total_diff):
            if i < math.floor(total_diff / 2):
                min_cost += difference[i][1]
            else:
                min_cost += difference[i][2]
        return min_cost