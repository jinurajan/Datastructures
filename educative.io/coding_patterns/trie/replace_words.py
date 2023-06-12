"""
"""

class TrieNode:
   def __init__(self):
       self.children = {}
       self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        # iterate over each character in the word we want to insert
        for c in word:
            # if the character doesn't belong to any child of the
            # current trie node, then create a new trie node for
            # this character as a child of the current node
            if c not in curr.children:
                curr.children[c] = TrieNode()

            # move to the child of the current node
            # (either already present or just added)
            curr = curr.children[c]
        # set flag end_of_word to TRUE to indicate we've reached
        # the end of inserted word
        curr.end_of_word = True

    # this function replaces each word in the sentence with
    # the smallest word from the dictionary
    def replace(self, word):
        curr = self.root
        # iterate over each dictionary word along
        # with the index of that character
        for i, c in enumerate(word):
            # if the character doesn't belong to the current node's children,
            # then return the word
            if c not in curr.children:
                return word

            # move to the child of the current node
            # corresponding to the current character
            curr = curr.children[c]
            # when the flag end_of_word becomes TRUE, this means
            # we've reached the end of word in the trie. If this is the
            # case, then return this word
            if curr.end_of_word:
                return word[:i+1]
        return word

    

def replace_words(sentence, dictionary):
   t = Trie()
   for prefix in dictionary:
      t.insert(prefix)
   
   result = []
   for word in sentence.split(" "):
      result.append(t.replace(word))
   
   return " ".join(result)
