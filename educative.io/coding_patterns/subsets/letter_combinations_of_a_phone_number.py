"""
Given a string having digits from 2-9 inclusive, return all the possible letter combinations that can be made from the numbers in the string. Return the answer in any order.

A mapping of digits to letters is given below.
Note: 
1 doesnt map to any letter.

"""


def letter_combinations(digits):
    # Write your code here
    char_map = {
        '1': [],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    result = []
    n = len(digits)
    combination = []
    def backtrack(index, combination):
        if index == n:
            result.append("".join(combination[:]))
            return
        for char in char_map[digits[index]]:
            combination.append(char)
            backtrack(index+1, combination)
            combination.pop()
    
    backtrack(0, combination)
    return result

def main():
    digits_array = ["2", "73", "426", "78", "925", "2345"]
    counter = 1
    for digits in digits_array:
        print(counter, ".\t All letter combinations for '",
              digits, "': ", letter_combinations(digits), sep="")
        counter += 1
        print("-" * 100)


if __name__ == "__main__":
    main()