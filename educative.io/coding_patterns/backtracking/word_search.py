"""
Given an m×n 2-D grid of characters, we have to find a specific word in the grid by combining the adjacent characters. Assume that only up, down, right, and left neighbors are considered adjacent.

m = board.length
n = board[i].length where 0 <= i < m
1 <=m, n<=6
1 <= word.length <= 15
board and word consists of only lowercase and upper case english letters
The search is not case sensitive
"""
def valid_indices(x, y, rows,cols):
    if x < rows and y < cols:
        return True
    return False

def traverse(x, y, idx, rows, cols, grid, word, visited):
    if idx == len(word):
        # found word
        return True
    if not valid_indices(x, y, rows, cols):
        return False
    if grid[x][y].lower() != word[idx].lower():
        return False
    visited.add((x, y))
    neighbours = {(0, -1), (-1, 0), (0, 1), (1, 0)}
    for dx, dy in neighbours:
        new_x, new_y = x+dx, y+dy
        if (new_x, new_y) not in visited:
            if traverse(new_x, new_y, idx+1, rows, cols, grid, word, visited) is True:
                return True
    return False
        
        
def word_search(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    start_char = word[0]
    start_indices_stack = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j].lower() == start_char.lower():
                start_indices_stack.append((i,j))
    if not start_indices_stack:
        return False
    if len(word) == 1 and start_indices_stack:
        return True
    while start_indices_stack:
        x, y = start_indices_stack.pop(0)
        if traverse(x,y, 0, rows, cols, grid, word, visited) is True:
            return True
        visited = set()
    return False

def main():
    input = [
             ([['E', 'D', 'X', 'I', 'W'],
              ['P', 'U', 'F', 'M', 'Q'],
              ['I', 'C', 'Q', 'R', 'F'],
              ['M', 'A', 'L', 'C', 'A'],
              ['J', 'T', 'I', 'V', 'E']], "educative"),

             ([['O', 'Y', 'O', 'I'],
              ['B', 'I', 'E', 'M'],
              ['K', 'D', 'Y', 'R'],
              ['M', 'T', 'W', 'I'],
              ['Z', 'I', 'T', 'O']], "DYNAMIC"),

             ([['h', 'e', 'c', 'm', 'l'],
              ['w', 'l', 'i', 'e', 'u'],
              ['a', 'r', 'r', 's', 'n'],
              ['s', 'i', 'i', 'o', 'r']], "WARRIOR"),

             ([['C', 'Q', 'N', 'A'],
              ['P', 'S', 'E', 'I'],
              ['Z', 'A', 'P', 'E'],
              ['J', 'V', 'T', 'K']], "save"),

             ([['A']], "ABC"),

             ([['P', 'S', 'S', 'I', 'W', 'P'],
              ['P', 'Y', 'C', 'A', 'Q', 'T'],
              ['I', 'S', 'H', 'P', 'F', 'Y'],
              ['M', 'T', 'O', 'L', 'O', 'I'],
              ['J', 'I', 'N', 'O', 'G', 'K'],
              ['I', 'M', 'D', 'T', 'Y', 'T']], "PSYCHOLOGY")
            ]
    num = 1

    for i in input:
        print(num, ".\tGrid =", sep="")
        for j in range(len(i[0])):
            print("\t\t", i[0][j])
        if i[1] == "":
            print('\n\tWord = ""')
        else:
            print(f"\n\tWord =  {i[1]}")
        print("\n\tProcessing...")
        search_result = word_search(i[0], i[1])
        if search_result:
            print("\n\tSearch result = Found Word")
        else:
            print("\n\tSearch result = Word couldn't found")
        num += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()
