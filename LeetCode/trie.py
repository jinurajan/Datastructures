"""
Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def char_to_index(self, char):
        return ord(char) - ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root
        for i in range(len(word)):
            index = self.char_to_index(word[i])
            if not root.children[index]:
                root.children[index] = self.getNode()
            root = root.children[index]
        root.is_end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for i in range(len(word)):
            index = self.char_to_index(word[i])
            if not root.children[index] or root.is_end_of_word:
                return False
            root = root.children[index]
        return root is not None and root.is_end_of_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for i in range(len(prefix)):
            index = self.char_to_index(prefix[i])
            if not root.children[index]:
                return False
            root = root.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# expected = [False,True,False,False,False,False,False,True,True,False,True,True,False,False,False,True,True,True]

# obj = Trie()
# obj.insert("app")
# obj.insert("apple")
# obj.insert("beer")
# obj.insert("add")
# obj.insert("jam")
# obj.insert("rental")
# i = 0
# print obj.search("apps"), "is equal to", expected[i]
# i += 1
# print obj.search("app"), "is equal to", expected[i]
# i += 1
# import pdb; pdb.set_trace()
# print obj.search("add"), "is equal to", expected[i]
# i += 1
# print obj.search("applepie"), "is equal to", expected[i]
# i += 1
# print obj.search("rest"), "is equal to", expected[i]
# i += 1
# print obj.search("jan"), "is equal to", expected[i]
# i += 1
# print obj.search("rent"), "is equal to", expected[i]
# i += 1
# print obj.search("beer"), "is equal to", expected[i]
# i += 1
# print obj.search("jam"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("apps"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("app"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("add"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("applepie"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("rest"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("jan"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("rent"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("beer"), "is equal to", expected[i]
# i += 1
# print obj.startsWith("jam"), "is equal to", expected[i]
# i += 1

obj = Trie()
ops = ["insert","search","search","startsWith","startsWith","insert","search","startsWith","insert","search","startsWith"]
inputs = [["ab"],["abc"],["ab"],["abc"],["ab"],["ab"],["abc"],["abc"],["abc"],["abc"],["abc"]]
outputs = [None,False,True,False,True,None,False,False,None,True,True]

for i in range(len(ops)):
    if ops[i] == "insert":
        print obj.insert(inputs[i][0]) == outputs[i]
    elif ops[i] == "search":
        print obj.search(inputs[i][0]) == outputs[i]
    else:
        print obj.startsWith(inputs[i][0]) == outputs[i]


