"""
Given two strings, check whether two strings are isomorphic to each other or not.  Two strings are isomorphic if a fixed mapping exists from the characters of one string to the characters of the other string. For example, if there are two instances of the character "a"  in the first string, both these instances should be converted to another character (which could also remain the same character if "a" is mapped to itself) in the second string. This converted character should remain the same in both positions of the second string since there is a fixed mapping from the character "a" in the first string to the converted character in the second string.
"""

def is_isomorphic(string1, string2):
  # Write your code here
  # your code will replace this placeholder return statement
  if len(string1) != len(string2):
    return False
  map_1 = {} # str1 to str2 mapping
  map_2 = {} # str2 to str1 mapping


  for i in range(len(string1)):
    char_1 = string1[i]
    char_2 = string2[i]
    if char_1 in map_1 and map_1[char_1] != char_2:
      return False
    if char_2 in map_2 and map_2[char_2] != char_1:
      return False
    
    map_1[char_1] = char_2
    map_2[char_2] = char_1


  return True  


def is_isomorphic(string1, string2):
  # Write your code here
  # your code will replace this placeholder return statement
  if len(string1) != len(string2):
    return False
  map_1 = {} # str1 to str2 mapping
  map_2 = {} # str2 to str1 mapping

  for char_1, char_2 in zip(string1,string2):
    if char_1 in map_1 and map_1[char_1] != char_2:
      return False
    if char_2 in map_2 and map_2[char_2] != char_1:
      return False
    
    map_1[char_1] = char_2
    map_2[char_2] = char_1


  return True  

