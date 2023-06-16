"""
You are given two integers, rows and cols, which represent the number of rows and columns in a 1-based binary matrix. In this matrix, each 
0 represents land, and each 1 represents water.


Initially, on day 0, the whole matrix will just be all 0s, that is, all land. With each passing day, one of the cells of this matrix will get flooded and, therefore, will change to water, that is, from 
0 to 1. This continues until the entire matrix is flooded. You are given a 1-based array, water_cells, that records which cell will be flooded on each day. Each element 
water_cells[i]=[ri,ci] indicates the cell present at the ri th row and ci th column of the matrix that will change from land to water on the 
i th day


We can cross any cell of the matrix as long as it’s land. Once it changes to water, we can’t cross it. To cross any cell, we can only move in one of the four cardinal directions. Given the number of rows and columns of a 1-based binary matrix and a 1-based array, water_cells, you are required to find the last day where you can still cross the matrix, from top to bottom, by walking over the land cells only.
"""


class UnionFind:
    def __init__(self, N):
        self.reps = []
        
        for i in range(N):
            self.reps.append(i)

    def find(self, x):
        if self.reps[x] != x:
            self.reps[x] = self.find(self.reps[x])
        return self.reps[x]

    def union(self, v1, v2):
        self.reps[self.find(v1)] = self.find(v2)

def last_day_to_cross(rows, cols, water_cells):
    day = 0
    matrix = [[0 for i in range(cols)]for j in range(rows)]
    # define two virtual nodes one before first column one after the last column
    left_node, right_node = 0, rows*cols+1

    def find_index(current_row, current_col):
        return current_row*cols + current_col+1
    
    def within_bounds(current_row, current_col):
        if 0 <= current_row < rows and 0 <= current_col < cols:
            return True
        return False
    
    # 8 directions
    directions = [(1,0), (0,1), (-1, 0), (0, -1), (1,1), (-1, 1), (1, -1), (-1,-1)]
    # convert to 0 based array
    water_cells = [(r-1, c-1) for r,c in water_cells]

    uf = UnionFind(rows*cols+2)
    for row, col in water_cells:
        matrix[row][col] = 1
    
        for dx, dy in directions:
            if within_bounds(row+dx, col+dy) and matrix[row+dx][col+dy] == 1:
                uf.union(find_index(row, col), find_index(row+dx, col+dy))
            if col == 0:
                uf.union(find_index(row, col), left_node)
            if col == cols-1:
                uf.union(find_index(row, col), right_node)
        
        # check if we got connected cells from left to right side
        if uf.find(left_node) == uf.find(right_node):
            break
        day += 1
    # replace this placeholder return statement with your code
    return day


# driver code
def main():
    all_water_cells = [[[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]],
                       [[1,1],[2,1],[1,2],[2,2]],
                       [[1,1],[1,2],[1,3],[2,1],[3,1],[2,2],[3,2],[2,3],[3,3]],
                       [[1,5],[2,5],[2,4],[2,3],[2,2],[3,2],[4,2],[4,1],[3,1],[2,1],[1,1],[1,2],[1,3],[1,4],
                        [3,3],[3,5],[3,4],[4,5],[4,3],[4,4]],
                       [[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[2,5],[2,6],[2,7],[3,1],[3,2],[3,3],[3,7],[4,7],
                        [4,5],[4,4],[4,3],[4,2],[4,1],[5,1],[5,2],[5,3],[5,4],[5,5],[5,7],[6,7],[7,7],[7,6],
                        [7,5],[7,4],[7,3],[7,2],[7,1],[6,1],[6,2],[6,3],[6,4],[6,5],[6,6],[5,6],[4,6],[3,6],
                        [3,5],[3,4],[2,4],[2,3],[2,2],[2,1],[1,1]],
                       [[3,2],[1,1],[1,2],[3,3],[2,3],[1,3],[2,1],[2,2],[3,1]]]
    all_rows = [3, 2, 3, 4, 7, 3]
    all_cols = [3, 2, 3, 5, 7, 3]
    
    for i in range(len(all_water_cells)):

        print(i+1, ".", "\tNumber of rows:",all_rows[i])
        print("\tNumber of columns:",all_cols[i])
        print("\n\tCells to be flooded: \n\t",all_water_cells[i])

        last_day = last_day_to_cross(all_rows[i], all_cols[i], all_water_cells[i])

        print("\n\tLast day where you can still cross:", last_day)
        print("-" * 100)

if __name__ == '__main__':
        main()