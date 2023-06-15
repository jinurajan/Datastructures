"""
Given two strings, a and b, return an array of all the start indexes of anagrams of b in a. We may return the answer in any order.

"""

from collections import Counter

def find_anagrams(a, b):
  if len(b) > len(a):
    return []
  result = []
  anagram_counter = Counter()
  b_counter = Counter(b)
  k = len(b)
  n = len(a)
  for end in range(n):
    anagram_counter[a[end]] += 1
    if end >= k:
      start = end - k
      if anagram_counter[a[start]] == 1:
        del anagram_counter[a[start]]
      else:
        anagram_counter[a[start]] -= 1
    
    if anagram_counter == b_counter:
      start = end - k + 1
      result.append(start)
  
  return result

# driver code
def main():
  A = ["abab", "cbaebabacd", "cefecf", "hello", "bro"]
  B = ["ab", "abc", "efc", "olleh", "bro"]
  for i in range(len(A)):
    print(i + 1, ".\tString a: \"", A[i], "\"", sep = "")
    print("\tString b: \"", B[i], "\"", sep = "")
    print("\tAnagrams of string b start at index(es) ", find_anagrams(A[i],B[i]), " in string a.", sep = "")
    print("-" * 100)

if __name__ == '__main__':
  main()