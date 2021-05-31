"""
Minimum Cost to Hire K Workers

There are n workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly k workers to form a paid group.  When hiring a group of k workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.



Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.


Note:

1 <= k <= n <= 10000, where n = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10-5 of the correct answer will be considered correct.


"""

from fractions import Fraction


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = sorted([(Fraction(w, q), q, w) for q, w in zip(quality, wage)])
        result = float("inf")
        max_heap = []
        total_wage = 0
        for ratio, q, w in workers:
            heapq.heappush(max_heap, -q)
            total_wage += q
            if len(max_heap) > k:
                total_wage += heapq.heappop(max_heap)
            if len(max_heap) == k:
                result = min(result, ratio * total_wage)
        return result







