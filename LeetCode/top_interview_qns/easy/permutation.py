

def permutations(a, l, r):
	if l == r:
		# reached the end of the string
		return array
	else:
		for i in xrange(l, r+1):
			a[i], a[l] = a[l], a[r]
			permutations(array, l+1, r)
			a[i], a[l] = a[l], a[r]
	return array