"""
Given a string, str, return the length of the longest substring without repeating characters.
"""
def find_longest_substring(str):
    if not str:
        return 0
    char_map = {}
    start, end = 0, 0
    longest_substring = 0
    while end < len(str):
        if str[end] in char_map:
            longest_substring = max(longest_substring, end-start)
            start = end
        char_map[str[end]] = end

        end += 1
    longest_substring = max(longest_substring, end-start)
    return longest_substring

# Driver code
def main():
    str = [
        "abcabcbb",
        "pwwkew",
        "bbbbb",
        "ababababa",
        "",
        "ABCDEFGHI",
        "ABCDEDCBA",
        "AAAABBBBCCCCDDDD",
    ]
    for i in range(len(str)):
        print(i + 1, ". \t Input String: ", str[i], sep="")
        print("\t Length of longest substring: ",
                (find_longest_substring(str[i])))
        print("-" * 100)


if __name__ == "__main__":
    main()