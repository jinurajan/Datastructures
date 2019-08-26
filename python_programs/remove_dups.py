"""
Write a script to remove all duplicate words from a string
"""


def RemoveDups(string):
    words = string.split()
    word_list = []
    for i in range(len(words)):
        if words[i] in word_list:
            # already exists. remove it
            pass
        else:
            word_list.append(words[i])
    return " ".join(word_list)


if __name__ == "__main__":
    print "Enter String:"
    string = raw_input()
    print RemoveDups(string)
