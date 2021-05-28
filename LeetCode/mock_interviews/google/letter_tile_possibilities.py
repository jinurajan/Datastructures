"""
Letter Tile Possibilities
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1


Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""
from typing import List

from itertools import permutations
from collections import Counter
import math

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len({x for i in range(1, len(tiles)+1) for x in permutations(tiles, i)})


class Solution1:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = Counter(tiles)
        print(freq)
        prod = 1
        for f in freq.values():
            prod *= f + 1
        print(prod)
        res = 0
        for i in range(1, prod):
            digits = []
            for f in freq.values():
                digits.append(i % (f + 1))
                i = i // (f + 1)
            tmp = math.factorial(sum(digits))
            for d in digits:
                tmp //= math.factorial(d)
            res += tmp
        return res


class Solution2:
    def numTilePossibilities(self, tiles: str) -> int:
        visited = defaultdict(lambda: False)
        result = set()

        def backtrack(index, n, chars):
            if chars:
                result.add("".join(chars[:]))
            for index in range(n):
                if not visited[index]:
                    chars.append(tiles[index])
                    visited[index] = True
                    backtrack(index + 1, n, chars)
                    visited[index] = False
                    chars.pop()

        backtrack(0, len(tiles), [])
        return len(result)



tiles = "AAB"
print(Solution1().numTilePossibilities(tiles))