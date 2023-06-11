"""
You’re given a list of words with lowercase English letters in a different order, written in an alien language. The order of the alphabet is some permutation of lowercase letters of the English language.

We have to return TRUE if the given list of words is sorted lexicographically in this alien language.

"""

def verify_alien_dictionary(words, order):
    if len(words) == 1:
        return True
    
    order_map = {}
    # create hashmap with indexes higher indexes used for order checking
    for index, val in enumerate(order):
        order_map[val] = index
    
    n = len(words)
    for i in range(n-1):
        for j in range(len(words[i])):
            if j >= len(words[i+1]):
                return False
            # compare first word with second if the order in first word char is > the second one means its fals
            if words[i][j] != words[i+1][j]:
                if order_map[words[i][j]] > order_map[words[i+1][j]]:
                    return False
                # 
                break
    return True


def verify_alien_dictionary(words, order):
    if len(words) == 1:
        return True
    
    order_map = {}
    # create hashmap with indexes higher indexes used for order checking
    for index, val in enumerate(order):
        order_map[val] = index
    
    for first, secnd in zip(words, words[1:]):
            for c, d in zip(first, secnd):
                if c != d:
                    if order_map[c] > order_map[d]:
                        return False
                    break
            else:
                if len(secnd) < len(first):
                    return False
    
    return True