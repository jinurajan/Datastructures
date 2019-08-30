

def add10(f):
	def decor(*args):
		return f(*args) + 10
	return decor


@add10
def add(a, b):
	return a + b






s = add(2, 3)
print "sum: ", s
print add.__name__
