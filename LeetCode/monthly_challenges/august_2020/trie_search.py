"""
Add and Search Word - Data structure design
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.end_of_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        root = self.root
        for w in word:
            index = ord(w) - ord('a')
            if not root.children[index]:
                root.children[index] = self.get_node()
            root = root.children[index]
        root.end_of_word = True

    def search(self, word, root=None):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # import pdb; pdb.set_trace()
        return self.search_pattern(self.root, word)

    def search_pattern(self, node, word):
        if not word and node.end_of_word:
            return True
        for i in range(len(word)):
            if word[i] == '.':
                new_word = ''.join(word[i + 1:])
                return any([self.search_pattern(each, new_word) for each in node.children if each])
            index = ord(word[i]) - ord('a')
            if not node.children[index]:
                return False
            node = node.children[index]
        if node.end_of_word:
            return True
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print obj.search("pad") == False
print obj.search(".ad") == True
print obj.search("b..") == True
print obj.search("p..") == False
print obj.search("...") == True
print obj.search("p.k") == False
