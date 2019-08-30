import re

s = "hi 1234 and 58789 done"

pattern = raw_input("Enter some pattern:")
result = re.findall(pattern, s)
print result