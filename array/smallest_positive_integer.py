


def solution(A):
	set_diff = set(xrange(1, len(A)+1)) - set(A)
	if set_diff:
		return min(set_diff)
	else:
		return A[-1] + 1




A = [1,3,6,4,1,2]
print solution(A)
A = [1, 2, 3]
print solution(A)
A = [-1, -3]
print solution(A)