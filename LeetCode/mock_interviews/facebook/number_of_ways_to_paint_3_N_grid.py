"""
Number of Ways to Paint N × 3 Grid
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
"""


class Solution:
    def numOfWays(self, n: int) -> int:
        f = g = 6
        M = 10 ** 9 + 7
        for _ in range(n - 1):
            f, g = (2 * f + 2 * g) % M, (2 * f + 3 * g) % M
        return (f + g) % M


def numOfWays(self, n: int) -> int:
    # Build a map of rows that are compatible
    rows = ['ryr', 'yry', 'gry', 'ryg', 'yrg', 'grg', 'rgr', 'ygr', 'gyr', 'rgy', 'ygy', 'gyg']
    compat = collections.defaultdict(list)
    compat[-1] = list(range(12))  # Because the first row can be any choice from rows
    for i in range(12):
        for j in range(i + 1, 12):
            if all(color1 != color2 for color1, color2 in zip(rows[i], rows[j])):
                compat[i].append(j)
                compat[j].append(i)

    # Top Down DP
    @functools.lru_cache(None)
    def helper(i, j):
        nonlocal n
        if i == n: return 1
        return sum(helper(i + 1, k) for k in compat[j])

    MOD = 10 ** 9 + 7
    return helper(0, -1) % MOD


from collections import defaultdict


class Solution:
    def numOfWays(self, n: int) -> int:
        CB = ['ryr', 'yry', 'gry', 'ryg', 'yrg', 'grg', 'rgr', 'ygr', 'gyr', 'rgy', 'ygy', 'gyg']
        HT = defaultdict(list)
        for i in range(12):
            for j in range(12):
                e1 = CB[i]
                e2 = CB[j]
                if i != j:
                    if e1[0] != e2[0]:
                        if e1[1] != e2[1]:
                            if e1[2] != e2[2]:
                                HT[i].append(j)

        md = 10 ** 9 + 7
        DP_MAT = [[0] * 12 for _ in range(n)]
        for j in range(12):
            DP_MAT[0][j] = 1

        for i in range(1, n):
            for j in range(12):
                for k in HT[j]:
                    DP_MAT[i][j] = DP_MAT[i][j] + DP_MAT[i - 1][k] % md

        return sum(DP_MAT[n - 1]) % md


Comments: 1
BestMost
VotesNewest
to
OldestOldest
to
Newest
Type
comment
here...(Markdown is supported)

Preview

Post
rowe1227
's avatar
rowe1227
Staff
1144
October
30, 2020
10: 13
PM

Read
More
Nice
solution! This is much
easier
to
follow
than
some
of
the
other
approaches.

Here is a
Top - Down
version
based
on
your
solution:


def numOfWays(self, n: int) -> int:
    # Build a map of rows that are compatible
    rows = ['ryr', 'yry', 'gry', 'ryg', 'yrg', 'grg', 'rgr', 'ygr', 'gyr', 'rgy', 'ygy', 'gyg']
    compat = collections.defaultdict(list)
    compat[-1] = list(range(12))  # Because the first row can be any choice from rows
    for i in range(12):
        for j in range(i + 1, 12):
            if all(color1 != color2 for color1, color2 in zip(rows[i], rows[j])):
                compat[i].append(j)
                compat[j].append(i)

    # Top Down DP
    @functools.lru_cache(None)
    def helper(i, j):
        nonlocal n
        if i == n: return 1
        return sum(helper(i + 1, k) for k in compat[j])

    MOD = 10 ** 9 + 7
    return helper(0, -1) % MOD


