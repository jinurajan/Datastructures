
def toInteger(List): 
    return [int(i) for i in List]


perm_set = []


def permutations(a, l, r):
    if l == r:
        # reached the end of the string
        perm_set.append(toInteger(a))
    else:
        for i in xrange(l, r+1):
            a[i], a[l] = a[l], a[i]
            permutations(a, l+1, r)
            a[i], a[l] = a[l], a[i]


if __name__ == "__main__":
    string = "abc"
    permutations(['1','2','3'], 0, len(string)-1)
    print perm_set
    perm_set = []
    permutations(['1','2','3', '4', '5', '6', '7', '8', '9','10', '11', '12'], 0, 11)
    print perm_set
    perm_set = []
    permutations(['11','22','13'], 0, len(string)-1)
    print perm_set