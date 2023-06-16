"""
Let’s consider a scenario with an (m×n) 2D grid containing binary numbers, where '0' represents water and '1' represents land. If any '1' cells are connected to each other horizontally or vertically (not diagonally), they form an island. Your task is to return the total number of islands in the grid.

"""
class UnionFind:

    # Initializing the parent list and count variable by traversing the grid
    def __init__(self, grid):
        self.parent = []
        self.rank = []
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j)
                    self.count += 1
                else:
                    self.parent.append(-1)
                self.rank.append(0)

    # Function to find the root parent of a node
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # Function to connect components
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

    # Function to return the number of conencted components consisting of "1"s
    def get_count(self):
        return self.count



def num_islands(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])

    union_find = UnionFind(grid)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                grid[row][col] = '0'

                if row-1 >= 0 and grid[row-1][col] == '1':
                    union_find.union(row * cols+col, (row-1)*cols+col)
                
                if row+1 < rows and grid[row+1][col] == '1':
                    union_find.union(row * cols+col, (row+1)*cols+col)
                
                if col-1 >=0 and grid[row][col-1] == '1':
                    union_find.union(row * cols+col, (row)*cols+col-1)
                
                if col+1 < cols and grid[row][col+1] == '1':
                    union_find.union(row * cols+col, (row)*cols+col+1)
    
    count = union_find.get_count()

    return count
                


def main():

    def print_grid(grid):
        for i in grid:
            print("\t", i)

    grid1 = [
        ['1', '1', '1'],
        ['0', '1', '0'],
        ['1', '0', '0'],
        ['1', '0', '1']
    ]

    grid2 = [
        ['1', '1', '1', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['1', '0', '0', '1', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '1']
    ]

    grid3 = [
        ['1', '1', '1', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '1']
    ]

    grid4 = [
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1']
    ]

    grid5 = [
        ['1', '0', '1'],
        ['0', '0', '0'],
        ['1', '0', '1']
    ]

    inputs = [grid1, grid2, grid3, grid4, grid5]
    num = 1
    for i in inputs:
        print(num, ".\tGrid:\n", sep = "")
        print_grid(i)
        print('\n\tOutput :', num_islands(i))
        print('-' * 100)
        num += 1


if __name__ == "__main__":
    main()
