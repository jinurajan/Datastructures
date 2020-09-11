"""
748. Shortest Completing Word (Easy)
Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.
Note:
licensePlate will be a string with length in range [1, 7].
licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
words will have a length in the range [10, 1000].
Every words[i] will consist of lowercase letters, and have length in range [1, 15].

"""

from copy import deepcopy


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        char_count = 0
        search_hash = {}
        for l in licensePlate:
            if l == " " or l.isdigit():
                continue
            val = l.lower()
            if val in search_hash:
                search_hash[val] += 1
            else:
                search_hash[val] = 1
            char_count += 1
        words = sorted(words, key=lambda x: len(x))
        for word in words:
            if len(word) < char_count:
                continue
            h = deepcopy(search_hash)
            for char in word:
                if not h:
                    # h has become empty
                    break
                if char in h:
                    h[char] -= 1
                    if h[char] == 0:
                        del h[char]
            if not h:
                return word

class Solution1(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        char_count = 0
        plate =[]
        for l in licensePlate:
            if l.isalpha():
                plate.append(l.lower())
        plate = sorted(plate)
        min_len = 1000
        index = -1
        for i in range(len(words)):
            word = words[i]
            if len(word) < len(plate):
                continue
            if len(word) < min_len:
                tmp = list(word.lower())
                j = 0
                while j < len(plate):
                    if plate[j] in tmp:
                        tmp.remove(plate[j])
                    else:
                        break
                    j += 1
                if j >= len(plate):
                    # all characters present
                    min_len = len(word)
                    index = i
        return words[index]





        
print Solution().shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"])
print Solution().shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"])

print Solution1().shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"])
print Solution1().shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"])

