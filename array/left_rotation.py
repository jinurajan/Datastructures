


n, d = raw_input().split()
n = int(n)
d = int(d)

array = raw_input().split()
print " ".join(x for x in array[d:]+array[:d])