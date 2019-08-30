import re

s = "hi 1234 and 58789 done"

pattern = raw_input("Enter some pattern:")
if re.search(pattern, s):
    print "found"
else:
    print "not found"
