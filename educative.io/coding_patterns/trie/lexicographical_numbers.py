"""
Given an integer value n, write a function that returns all the numbers in the range 1 to n in lexicographical order.
"""


class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_complete = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def get_integers(self, value):
        result = []
        while value:
            value, integer = divmod(value, 10)
            result.append(integer)
        return result[::-1]
        
    
    # Function to insert a string in the trie
    def insert(self, number):
        node = self.root
        print(self.get_integers(number))
        for c in self.get_integers(number):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)
        node.is_complete = True
    
    # Function to search a string from the trie
    def search(self, number):
        node = self.root
        for c in self.get_integers(number):
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.is_complete
    
    # Function to search prefix of strings
    def starts_with(self, prefix):
        node = self.root
        for c in self.get_integers(prefix):
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True

def format(list_integer):
    result = 0
    power = 0
    for i in list_integer[::-1]:
        result += i * pow(10, power)
        power += 1
    return result

def lexicographical_order(n):
    trie = Trie()
    for i in range(1, n+1):
        trie.insert(i)
    result = []
    values = []
    def dfs(node, values):
        if not node:
            return
        if node.is_complete:
            result.append(format(values[:]))
        for child in sorted(node.children):
            values.append(child)
            dfs(node.children[child], values)
            values.pop()
    
    dfs(trie.root, [])
    return result

# def lexicographical_order(n):
#     ans = []
#     def dfs(s):
#         ans.append(int(s))
#         for i in range(10):
#             if(int(s+str(i)) > n):
#                 return
#             else:
#                 if(s):
#                     dfs(s+str(i))
#     for i in range(1, min(n+1, 10)):
#         dfs(str(i))
    
#     return ans


lexicographical_order(12)