"""
    Write a script to find the frequency occurrence of words from a given string
"""


def frequency_of_word(array):
    hash_map = {}
    for i in range(len(array)):
        if array[i] in hash_map:
            hash_map[array[i]] += 1
        else:
            hash_map[array[i]] = 1
    return hash_map


if __name__ == "__main__":
    print "Enter String:"
    string = raw_input()
    strings = string.split()
    print frequency_of_word(strings)