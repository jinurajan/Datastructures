"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". The magazine has all the right words, but there's a case mismatch. The answer is .

Function Description

Complete the checkMagazine function in the editor below. It must print  if the note can be formed using the magazine, or .

checkMagazine has the following parameters:

magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note
Input Format

The first line contains two space-separated integers,  and , the numbers of words in the  and the .. 
The second line contains  space-separated strings, each . 
The third line contains  space-separated strings, each .

Constraints

.
Each word consists of English alphabetic letters (i.e.,  to  and  to ).
Output Format

Print Yes if he can use the magazine to create an untraceable replica of his ransom note. Otherwise, print No.

Sample Input 0

6 4
give me one grand today night
give one grand today
Sample Output 0

Yes
Sample Input 1

6 5
two times three is not four
two times two is four
Sample Output 1

No
Explanation 1

'two' only occurs once in the magazine.

Sample Input 2

7 4
ive got a lovely bunch of coconuts
ive got some coconuts
Sample Output 2

No
Explanation 2

Harold's magazine is missing the word .
"""

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_hash = {}
    note_hash = {}
    for each in magazine:
        if each not in magazine_hash:
            magazine_hash[each] = 1
        else:
            magazine_hash[each] = magazine_hash[each] + 1

    for each in note:
        if each not in note_hash:
            note_hash[each] = 1
        else:
            note_hash[each] = note_hash[each] + 1

    for each in note_hash:
        if each not in magazine_hash or note_hash[each] > magazine_hash[each]:
            return "No"

    return "Yes"


if __name__ == '__main__':
    # mn = raw_input().split()

    # m = int(mn[0])

    # n = int(mn[1])

    # magazine = raw_input().rstrip().split()

    # note = raw_input().rstrip().split()
    magazine = ["two", "times", "three", "is", "not", "four"]
    note = ["two", "times", "two", "is", "four"]

    print checkMagazine(magazine, note)

    magazine = ["give", "me", "one", "grand", "today", "night"]
    note = ["give", "one", "grand", "today"]

    print checkMagazine(magazine, note)
