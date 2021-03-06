"""
Short Encoding of Words

A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.
"""
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        if len(words) == 1:
            return len(words[0]) + 1
        uniq_words = list(set(words))
        for word in words:
            for k in range(1, len(word)):
                if word[k:] in uniq_words:
                    uniq_words.remove(word[k:])
        return sum(len(word)+1 for word in uniq_words)


from collections import defaultdict
from functools import reduce
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        import pdb; pdb.set_trace()
        words = list(set(words))
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        # nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
        # return sum(len(word)+1 for i, word in enumerate(words) if len(nodes[i]) == 0)
        nodes = []
        for word in words:
            nodes.append(reduce(dict.__getitem__, word[::-1], trie))
        s =  0
        for i, word in enumerate(words):
            if not len(nodes[i]):
                s += len(word) + 1
        return s





words = ["time", "me", "bell"]
print(Solution().minimumLengthEncoding(words))

# words = ['t']
# print(Solution().minimumLengthEncoding(words))
#
# words = ['time', 'time']
# print(Solution().minimumLengthEncoding(words))
#
# words = ['belltime', 'time', 'me', 'be']
# print(Solution().minimumLengthEncoding(words))

