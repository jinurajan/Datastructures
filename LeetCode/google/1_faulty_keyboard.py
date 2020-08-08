"""
Given a string which is the sentence typed using that keyboard and a dictionary of valid words, return all possible correct formation of the sentence.

Example:

Input: s = "I lik   to   xplor   univ rs ", dictionary  = {"like", "explore", "toe", "universe", "rse"}
Output:
["I like to explore universe",
"I like toe xplor  universe",
"I like to explore univ rse",
"I like toe xplor  univ rse"]
There are two spaces after "lik", "to" and before "univ" in the sentence indicating one is actual space and another one is resulted by hitting key 'e'.

NOTE: dictionary only have words with 'e' in it if it does not exist in dictionary consider as valid case
"""


def generate_strings(string, index, hash_set, result):
    if index != len(string) - 1:
        words = string.split(" ")
        for word in words:
            if word not in hash_set:
                return
        result.append(string)
        print result
        return
    generate_strings(string, index + 1, hash_set, result)
    if string[index] == ' ':
        string[index] = 'e'
        generate_strings(string, index + 1, hash_set, result)
        string[index] = ' '


if __name__ == "__main__":
    string = "I lik   to   xplor   univ rs  "
    hash_set = set(["I", "like", "to", "explore", "xplore", "toe", "universe", "rse"])
    result = []
    import pdb; pdb.set_trace()
    generate_strings(string, 0, hash_set, result)
    print ''.join(result)
