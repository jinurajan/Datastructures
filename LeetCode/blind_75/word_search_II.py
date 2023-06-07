"""
Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

m == board.length
n == board[i].length

1 <= m, n <= 12
board[i][j] is a lowercase English letter.

1 <= words.length <= 3 * 104
1 <= words[i].length <= 10

words[i] consists of lowercase English letters.
All the strings of words are unique.


Thoughts
1. create a set out of words to easy matching with O(1)
2. traverse through board (bfs / dfs) marking visited cells and if the constructed words is in words pop from the set and add it to the result list
"""
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'

        trie = {}
        # create trie from all possible words
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[WORD_KEY] = word #instead of 1 store entire word as the value
        
        rows = len(board)
        cols = len(board[0])

        matched_words = []

        def valid(x, y):
            if 0 <= x <= rows-1 and 0 <=y <= cols-1:
                return True
            return False

        def backtracking(x, y, parent):
            char = board[x][y]
            curr_node = parent[char]
            
            # check if there is an match of word
            word_match = curr_node.pop(WORD_KEY, False)
            if word_match:
                # found match add it to result list
                matched_words.append(word_match)
            
            # mark the node as visited by marking '#
            board[x][y] = '#'

            # explore all neighbours
            for dx, dy in ([(0,1), (1,0), (0,-1), (-1, 0)]):
                new_x, new_y = x+dx, y+dy
                if not valid(new_x, new_y):
                    continue
                if not board[new_x][new_y] in curr_node:
                    continue
                backtracking(new_x, new_y, curr_node)
            # finished exploration set it back
            board[x][y] = char

            # optimization, incrementally remove the matched lead node in trie
            if not curr_node:
                parent.pop(char)
            
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return matched_words
