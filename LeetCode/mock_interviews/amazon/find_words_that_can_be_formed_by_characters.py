"""
 Find Words That Can Be Formed by Characters

 you are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_counter = Counter(chars)
        count = 0
        for word in words:
            counter_copy = deepcopy(char_counter)
            all_present = True
            for char in word:
                if char in counter_copy and counter_copy[char] >= 0:
                    counter_copy[char] -= 1
                    if counter_copy[char] == 0:
                        del counter_copy[char]
                else:
                    all_present = False
                    break
            if counter_copy and all_present:
                count += len(word)
        return count

