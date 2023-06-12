"""
You are given a list of strings that you need to find in a 2D grid of letters such that the string can be constructed from letters in sequentially adjacent cells. The cells are considered sequentially adjacent when they are neighbors to each other either horizontally or vertically. The solution should return a list containing the strings from the input list that were found in the grid

"""

from trie import Trie

def find_strings(grid, words):
    # grid is a 2D array of characters
    # strings is the list of strings that we are searching for
    # write your code here
    trie = Trie()
    result = []
    for word in words:
        trie.insert(word) 

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            dfs(trie, trie.root, grid, i, j, result) 
    return result

def dfs(trie, node, grid, row, col, result, word=''):
    if node.is_string:
        result.append(word)
        node.is_string = False
        trie.remove_characters(word)
    
    if 0 <= row < len(grid) and 0<= col < len(grid[0]):
        char = grid[row][col]
        child = node.children.get(char)
        if child:
            word += char
            grid[row][col] = None
            for dx, dy in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                dfs(trie, child, grid, row +dx, col+dy, result, word)
            grid[row][col] = char


def print_grid(grid):
    for i in grid:
        output = '   '.join(i)
        print("\t", output)


# Driver Code
def main():
    test_case_grid = [
        [['B', 'S', 'L', 'I', 'M'], 
        ['R', 'I', 'L', 'M', 'O'], 
        ['O', 'L', 'I', 'E', 'O'], 
        ['R', 'Y', 'I', 'L', 'N'], 
        ['B', 'U', 'N', 'E', 'C']],

        [['C', 'S', 'L', 'I', 'M'], 
        ['O', 'I', 'B', 'M', 'O'], 
        ['O', 'L', 'U', 'E', 'O'], 
        ['N', 'L', 'Y', 'S', 'N'], 
        ['S', 'I', 'N', 'E', 'C']],

        [['C', 'O', 'L', 'I', 'M'], 
        ['I', 'N', 'L', 'M', 'O'], 
        ['A', 'L', 'I', 'E', 'O'], 
        ['R', 'T', 'A', 'S', 'N'], 
        ['S', 'I', 'T', 'A', 'C']],

        [['P', 'S', 'L', 'A', 'M'], 
        ['O', 'P', 'U', 'R', 'O'], 
        ['O', 'L', 'I', 'E', 'O'], 
        ['R', 'T', 'A', 'S', 'N'], 
        ['S', 'I', 'T', 'A', 'C']],

        [['O', 'A', 'A', 'N'],
        ['E', 'T', 'A', 'E'],
        ['I', 'H', 'K', 'R'],
        ['I', 'F', 'L', 'V']],

        [['S', 'T', 'R', 'A', 'C'],
        ['I', 'R', 'E', 'E', 'E'],
        ['N', 'G', 'I', 'T', 'C'],
        ['I', 'T', 'S', 'R', 'A']],

        [['A', 'A', 'A'],
        ['A', 'A', 'A'],
        ['A', 'A', 'A']]
    ]

    strings_to_search = [
        ["BUY", "SLICK", "SLIME", "ONLINE", "NOW"],
        ["BUY", "STUFF", "ONLINE", "NOW"],
        ["REINDEER", "IN", "RAIN"],
        ["TOURISM", "DESTINY", "POPULAR"],
        ["OATH", "PEA", "EAT", "RAIN"],
        ["STREET", "STREETCAR", "STRING", "STING", "RING", "RACECAR"],
        ["A", "AA", "AAA", "AAAA"]
    ]

    for i in range(len(test_case_grid)):
            if i > 0:
                print()
            print(i + 1, ".\t2D Grid:\n", sep="")
            print_grid(test_case_grid[i])
            print("\n\tInput list: ", strings_to_search[i])
            print("\n\tOutput: ", find_strings(test_case_grid[i], strings_to_search[i]))
            print("-"*100) 


if __name__ == '__main__':
    main()
