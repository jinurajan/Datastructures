"""
Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

"""


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        row = len(grid)
        column = len(grid[0])
        print row, column
        self.counter = 0
        self.non_zero = 0
        self.hash_set = {}
        new_indices = []
        for i in range(row):
            for j in range(column):
                print i, j
                if grid[i][j] != 0:
                    self.non_zero += 1
                if grid[i][j] == 2:
                    self.hash_set[(i, j)] = 1
                    self.marked_adjascents(
                        grid, i, j, row - 1, column - 1, new_indices)
        if len(self.hash_set) == self.non_zero:
            return 0
        self.counter += 1
        # do it until new indices set is empty or non_zero element is equal
        # to len of the hash_set of 2 valued indices
        for iteration in range(1, row * column + 1):
            newest_indices = []
            for indices in new_indices:
                i, j = indices
                grid[i][j] = 2
                self.hash_set[(i, j)] = 1
                if len(self.hash_set) == self.non_zero:
                    return self.counter
                self.marked_adjascents(
                    grid, i, j, row - 1, column - 1, newest_indices)
            new_indices = newest_indices
            if not new_indices:
                if len(self.hash_set) != self.non_zero:
                    return -1
                return self.counter
            self.counter += 1
        return self.counter

    def marked_adjascents(self, a, i, j, r, c, indices_array):
        all_zero = True
        four_dimensional_adj = {(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)}
        for each in four_dimensional_adj:
            row = each[0]
            column = each[1]
            if row >= 0 and row <= r and column >= 0 and column <= c:
                if a[row][column] != 0:
                    all_zero = False
                if a[i][j] == 2 and a[row][column] == 1:
                    indices_array.append([row, column])
        return all_zero


if __name__ == "__main__":
    array = [[2,1,1],[1,1,0],[0,1,1]]
    print Solution().orangesRotting(array)
    array = [[2,1,1],[0,1,1],[1,0,1]]
    print Solution().orangesRotting(array)
    array = [[0, 2]]
    print Solution().orangesRotting(array)
