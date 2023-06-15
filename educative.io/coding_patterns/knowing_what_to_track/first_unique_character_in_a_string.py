"""
For a given string of characters, s, your task is to find the first non-repeating character and return its index. Return 1
if there is no unique character in the given string.

Only lowercase english letters are accepted.
There are no spaces in the string.
"""

from collections import Counter
def first_unique_char(s):

    word_counter = Counter(s)
    for idx, num in enumerate(s):
        if word_counter[num] == 1:
            return idx

    return -1

# driver code
def main():
    str_array = ["baefeab", "aabbcc", "dajhfiuebdafsdhdgaj",
                 "xyurtwxwtryua", "aeiouqwertyauieotweryqq", "awsjuhfajwfnkag"]

    for i in range(len(str_array)):
        print(i + 1, ".\t Input string: \"", str_array[i], "\"", sep="")
        result = first_unique_char(str_array[i])
        print("\t Finding a unique character .....")
        print("\t Index of the first unique character is: ", result, sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
