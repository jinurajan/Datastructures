"""
Prison Cells After N Days

There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells[i] == 1 if the ith cell is occupied and cells[i] == 0 if the ith cell is vacant, and you are given an integer n.

Return the state of the prison after n days (i.e., n such changes described above).

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], n = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
Example 2:

Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
Output: [0,0,1,1,1,1,1,0]


Constraints:

cells.length == 8
cells[i] is either 0 or 1.
1 <= n <= 109

"""
from typing import List


class Solution1:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = dict()
        is_fast_forwarded = False

        while n > 0:
            # we only need to run the fast-forward once at most
            if not is_fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    # the length of the cycle is seen[state_key] - N
                    n %= seen[state_key] - n
                    is_fast_forwarded = True
                else:
                    seen[state_key] = n

            # check if there is still some steps remained,
            # with or without the fast-forwarding.
            if n > 0:
                n -= 1
                next_day_cells = self.nextDay(cells)
                cells = next_day_cells

        return cells

    def nextDay(self, cells: List[int]):
        ret = [0]  # head
        for i in range(1, len(cells) - 1):
            ret.append(int(cells[i - 1] == cells[i + 1]))
        ret.append(0)  # tail
        return ret

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = dict()
        is_fast_forwarded = False

        # step 1). convert the cells to bitmap
        state_bitmap = 0x0
        for cell in cells:
            state_bitmap <<= 1
            state_bitmap = (state_bitmap | cell)

        # step 2). run the simulation with hashmap
        while N > 0:
            if not is_fast_forwarded:
                if state_bitmap in seen:
                    # the length of the cycle is seen[state_key] - N
                    N %= seen[state_bitmap] - N
                    is_fast_forwarded = True
                else:
                    seen[state_bitmap] = N
            # if there is still some steps remained,
            #   with or without the fast-forwarding.
            if N > 0:
                N -= 1
                state_bitmap = self.nextDay(state_bitmap)

        # step 3). convert the bitmap back to the state cells
        ret = []
        for i in range(len(cells)):
            ret.append(state_bitmap & 0x1)
            state_bitmap = state_bitmap >> 1

        return list(reversed(ret))


    def nextDay(self, state_bitmap: int):
        state_bitmap = ~ (state_bitmap << 1) ^ (state_bitmap >> 1)
        state_bitmap = state_bitmap & 0x7e  # set head and tail to zero
        return state_bitmap


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        visited = dict()
        is_repeated_call = False

        state_bitmap = 0x0
        # convert into bitmap
        for cell in cells:
            state_bitmap <<= 1
            state_bitmap = (state_bitmap | cell)

        while N > 0:
            if not is_repeated_call:
                if state_bitmap in visited:
                    N %= visited[state_bitmap] - N
                    is_repeated_call = True
                else:
                    visited[state_bitmap] = N
            if N > 0:
                N -= 1
                state_bitmap = self.next_day(state_bitmap)
        result = []
        for i in range(len(cells)):
            result.append(state_bitmap & 0x1)
            state_bitmap = state_bitmap >> 1
        return list(reversed(result))

    def next_day(self, state_bitmap):
        state_bitmap = ~ (state_bitmap << 1) ^ (state_bitmap >> 1)
        state_bitmap = state_bitmap & 0x7e
        return state_bitmap


cells = [0,1,0,1,1,0,0,1]
N = 7
print(Solution().prisonAfterNDays(cells, N))