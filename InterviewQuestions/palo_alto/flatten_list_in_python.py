"""
Flatten list in python with and without using inbuilt methods
"""

output = []

def flatten_list(l):
	for i in l:
		if type(i) == list:
			flatten_list(i)
		else:
			output.append(i)




def flatten_list_1(l, result):
	for i in l:
		if type(i) == list:	
			flatten_list_1(i, result)
		else:
			result.append(i)


flatten_list([[1, 2], 3, 4])
print output
result = []
flatten_list_1([[1, 2], 3, 4], result)
print result