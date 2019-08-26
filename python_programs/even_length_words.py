"""
    Write a script to find the number of even length words from a given string 
"""


def even_length_words(string):
    words = string.split()
    count = 0
    for each in words:
        if len(each) % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    print "Enter String:"
    string = raw_input()
    print even_length_words(string)
