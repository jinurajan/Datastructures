import re


def find_all_words_containing_vowel(string):
    pattern = r"\b[A-Za-z0-9_]*[AEIOUaeiou]{1}\b"
    result = re.findall(pattern, string)
    return result


if __name__ == "__main__":
    print "Enter string:"
    input_val = raw_input()
    print find_all_capital_words_ending_with_vowel(input_val)
