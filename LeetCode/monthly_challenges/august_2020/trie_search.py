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
        self.is_end_of_word = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def char_to_int(self, char):
        return ord(char) - ord('a')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        root = self.root
        for i in range(len(word)):
            index = self.char_to_int(word[i])
            if not root.children[index]:
                root.children[index] = self.getNode()
            root = root.children[index]
        root.is_end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for i in range(len(word)):
            if word[i] == '.':
                # check if children is not empty
                continue
            index = self.char_to_int(word[i])
            if not root.children[index]:
                return False
            root = root.children[index]
        return root.is_end_of_word


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print obj.search("pad")
print obj.search(".ad")
print obj.search("b..")
