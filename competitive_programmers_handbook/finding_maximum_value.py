"""

"""

def find_max_value(n):
    x = -1
    start = n
    while start >= 1:
        while func(start+x) < func(start+x+1):
            x += start
        start //= 2
    return x+1