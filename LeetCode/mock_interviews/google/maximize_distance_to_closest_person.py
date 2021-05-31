"""
Maximize Distance to Closest Person
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.


"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans, seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K + 1) / 2)

        return int(ans)


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        left, right = [N] * N, [N] * N

        for i in range(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        for i in range(N - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N - 1:
                right[i] = right[i + 1] + 1

        return max(min(left[i], right[i])
                   for i, seat in enumerate(seats) if not seat)
