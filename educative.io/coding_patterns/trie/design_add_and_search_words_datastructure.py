"""
Design a data structure called WordDictionary that supports the following functionalities:

Constructor: This function will initialize the object.

Add Word(word): This function will store the provided word in the data structure.

Search Word(word): This function will return TRUE if any string in the WordDictionary object matches the query word. Otherwise, it will return FALSE. If the query word contains dots, ., each dot is free to match any letter of the alphabet.

For example, the dot in the string “.ad” can have 26 ossible search results like “aad”, “bad”, “cad”, and so on.

Get Words(): This function will return all the words in the WordDictionary class.
"""


# TrieNode template class
class TrieNode():
  
  # Initialize TrieNode instance
  def __init__(self):
    # Empty list of child nodes
    self.children = []
    # False indicates this node is not the end of a word
    self.complete = False
    # Create 26 child nodes for each letter of alphabet
    for i in range(0, 26):
      self.children.append(None)


# Tip: You may use some of the code templates provided
# in the support files

class WordDictionary:
  def __init__(self):
    # Initialize your variables here
    self.root = TrieNode()
    self.can_find = False

  def add_word(self, word):
    # write your code here
    n = len(word)
    node = self.root
    for idx, char in enumerate(word):
      index = ord(char) - ord('a')
      if not node.children[index]:
        node.children[index] = TrieNode()
      node = node.children[index]
      if idx == n-1:
        if node.complete:
          return
        node.complete = True
    
  def search_helper(self, root, word, i):
    if self.can_find:
      return
    if not root:
      return
    
    if len(word) == i:
      if root.complete:
        self.can_find = True
      
      return
    
    if word[i] == '.':
      for j in range(ord('a'), ord('z')+1):
        self.search_helper(root.children[j - ord('a')], word, i+1)
    else:
      index = ord(word[i]) - ord('a')
      self.search_helper(root.children[index],word, i+1)

  def search_word(self, word):
    self.can_find = False
    self.search_helper(self.root, word, 0)
    return self.can_find
  
  def dfs(self, root, word,words_list):
    if not root:
      return words_list
    if root.complete:
      words_list.append(word)
    
    for j in range(ord('a'), ord('z')+1):
      prefix = word + chr(j)
      words_list = self.dfs(root.children[j-ord('a')], prefix, words_list)
    
    return words_list


  def get_words(self):
    # write your code here
    words_list = []
    if not self.root:
      return []
    return self.dfs(self.root, "", words_list)
  