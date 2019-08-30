import re

s = "hi 1234 and 58789 done"

pattern = raw_input("Enter some pattern:")
s1 = re.sub(pattern, "ABC", s)
print s1 # hi ABC and ABC done

t = re.subn(pattern, "ABC", s)
# returns tuple with new string and number of occurences



t = re.subn(pattern, "ABC", s, 4)


