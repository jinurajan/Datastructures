"""
Given a list of words or phrases, group the words that are anagrams of each other. An anagram is a word or phrase formed from another word by rearranging its letters.
"""

from collections import defaultdict

def group_anagrams(strs):
    anagram_map = defaultdict(list)
    for word in strs:
        count =[0] * 26
        for char in word:
            count[ord(char)-ord('a')] += 1
        
        anagram_map[tuple(count)].append(word)
    
    return list(anagram_map.values())


def group_anagrams(strs):

    anagram_map = defaultdict(list)
    for word in strs:
        sorted_word = "".join(sorted(word))
        anagram_map[sorted_word].append(word)

    return [a for a in anagram_map.values()]