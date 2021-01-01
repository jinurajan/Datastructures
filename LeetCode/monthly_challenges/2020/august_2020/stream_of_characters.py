"""
Stream of Characters
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); # init the dictionary.
streamChecker.query('a');          # return false
streamChecker.query('b');          # return false
streamChecker.query('c');          # return false
streamChecker.query('d');          # return true, because 'cd' is in the wordlist
streamChecker.query('e');          # return false
streamChecker.query('f');          # return true, because 'f' is in the wordlist
streamChecker.query('g');          # return false
streamChecker.query('h');          # return false
streamChecker.query('i');          # return false
streamChecker.query('j');          # return false
streamChecker.query('k');          # return false
streamChecker.query('l');          # return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
"""

class TrieNode(object):
    def __init__(self):
        self.children = [0] * 26
        self.end_of_word = False


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = self.get_node()
        self.last_queried = set([self.root])
        for word in words:
            self.insert(word)

    def get_node(self):
        return TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
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

    def check_for_char(self, root, w):
        index = ord(w) - ord('a')
        if not root.children[index]:
            return False
        root = root.children[index]
        self.last_queried.add(root)
        if root:
            if root.end_of_word:
                return True
            else:
                return False
        else:
            return False

    def query(self, w):
        """
        :type letter: str
        :rtype: bool
        """
        for root in self.last_queried:
            return self.check_for_char(root, w)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
streamChecker = StreamChecker(["cd","f","kl"]) # init the dictionary.
print streamChecker.query('a')          # return false
print streamChecker.query('b')          # return false
print streamChecker.query('c')          # return false
print streamChecker.query('d')          # return true, because 'cd' is in the wordlist
print streamChecker.query('e')          # return false
print streamChecker.query('f')          # return true, because 'f' is in the wordlist
print streamChecker.query('g')          # return false
print streamChecker.query('h')          # return false
print streamChecker.query('i')          # return false
print streamChecker.query('j')          # return false
print streamChecker.query('k')          # return false
print streamChecker.query('l')          # return true, because 'kl' is in the wordlist
