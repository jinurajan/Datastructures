import re


def find_all_capital_words_ending_with_vowel(string):
    # pattern = "\s?[A-Z]+[A-Za-z0-9_]*[aeiou]{1}\s?|$"
    pattern = r"\b[A-Z]+[A-Za-z0-9_]*[aeiou]\b"
    result = re.findall(pattern, string)
    return result


if __name__ == "__main__":
    print "Enter string:"
    input_val = raw_input()
    print find_all_capital_words_ending_with_vowel(input_val)
