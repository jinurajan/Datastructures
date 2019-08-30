import re


def find_all_capital_words(string):
    pattern = r"\b[A-Z]+[A-Za-z0-9_]*\b"
    result = re.findall(pattern, string)
    return result


if __name__ == "__main__":
    print "Enter string:"
    input = raw_input()
    print find_all_capital_words(input)