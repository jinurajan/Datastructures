"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Example 1:

Input: "ad52"
Output: "ad52", "Ad52", "aD52", "AD52"
Example 2:

Input: "ab7c"
Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
"""


def find_letter_case_string_permutations(str):
    permutations = []

    def backtrack(str, index, perm):
        if index == len(str):
            permutations.append(perm)
            return
        else:
            backtrack(str, index + 1, perm + str[index])
            if str[index].isalpha():
                backtrack(str, index + 1, perm + str[index].upper())

    backtrack(str, 0, "")
    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
