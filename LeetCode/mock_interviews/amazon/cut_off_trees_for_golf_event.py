"""
Cut Off Trees for Golf Event
You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

0 means the cell cannot be walked through.
1 represents an empty cell that can be walked through.
A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.

Input: forest = [[1,2,3],[0,0,4],[7,6,5]]
Output: 6
Explanation: Following the path above allows you to cut off the trees from shortest to tallest in 6 steps.

Input: forest = [[1,2,3],[0,0,0],[7,6,5]]
Output: -1
Explanation: The trees in the bottom row cannot be accessed as the middle row is blocked.
Example 3:

Input: forest = [[2,3,4],[0,0,5],[8,7,6]]
Output: 6
Explanation: You can follow the same path as Example 1 to cut off all the trees.
Note that you can cut off the first tree at (0, 0) before making any steps.


Constraints:

m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109
"""


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        validTraversals = defaultdict(list)

        # checks if cell is valid
        def isValidCell(arr, cell):
            return 0 <= cell[0] < len(arr) and 0 <= cell[1] < len(arr[0]) and arr[cell[0]][cell[1]] != 0

        # bfs to find shortest path to target cell
        def movesToReachTarget(arr, targetCell, currentCell):
            seen = set()
            tovisit = [currentCell]
            moves = 0
            while (tovisit):
                newcells = deque()
                for cell in tovisit:
                    if cell == targetCell:
                        return moves
                    for neighborcell in validTraversals[(cell[0], cell[1])]:
                        if (neighborcell[0], neighborcell[1]) not in seen:
                            seen.add((neighborcell[0], neighborcell[1]))
                            newcells.append(neighborcell)
                tovisit = newcells
                moves += 1
            return -1

        trees = []
        treesdict = {}
        moves = 0
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        # get list of tree heights and position of each tree
        # get valid moves for each open position
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j] > 1:
                    trees.append(forest[i][j])
                    treesdict[forest[i][j]] = [i, j]
                if forest[i][j] > 0:
                    for _dir in dirs:
                        if isValidCell(forest, [i + _dir[0], j + _dir[1]]):
                            validTraversals[(i, j)].append([i + _dir[0], j + _dir[1]])
        trees = sorted(trees)
        pos = [0, 0]
        for tree in trees:
            movesToNextTree = movesToReachTarget(forest, treesdict[tree], pos)
            if movesToNextTree < 0:
                return -1
            moves += movesToNextTree
            pos = treesdict[tree]
        return moves