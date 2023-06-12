"""
Trie is a tree-like data structure used to store strings. The tries are also called prefix trees because they provide very efficient prefix-matching operations. Implement a trie data structure with three functions that perform the following tasks:

Insert (word): This inserts a word into the trie.
Search (word): This searches the given word in the trie and returns TRUE, if found. Otherwise, return FALSE.
Search prefix (prefix): This searches the given prefix in the trie and returns TRUE, if found. Otherwise, return FALSE.

"""




class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, string):
        root = self.root
        for char in string:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.is_word = True
    
    def search(self, string):
        root = self.root
        for char in string:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.is_word
    
    def search_prefix(self, prefix):
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True
