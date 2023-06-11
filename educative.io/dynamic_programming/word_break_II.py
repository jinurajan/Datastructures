"""
You are given a string, s, and an array of strings, word_dict, representing a dictionary. Your task is to add spaces to s to break it up into a sequence of valid words from word_dict. We are required to return an array of all possible sequences of words (sentences). The order in which the sentences are listed is not significant.

"""



def word_break(s, word_dict):
    word_dict = set(word_dict)
    n = len(s)
    dp = [[]] * (n+1)
    dp[0] = [""]

    for i in range(1, n+1):
        prefix = s[:i]
        temp = []
        for j in range(i):
            suffix = prefix[j:]
            if suffix in word_dict:
                for substring in dp[j]:
                    temp.append((substring + " " + suffix).strip())
        dp[i] = temp
    
    return dp[n]
