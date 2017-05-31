# Problem Definition: http://www.geeksforgeeks.org/majority-element/

# METHOD 1 (Basic)
# Complexity O(n*n)
# Space Complexity: O(1)
def find_majority_element(array):

	n = len(array)
	ele_factor = n/2
	for i in range(n):
		current_element = array[i]
		count = 0
		for j in range(n):
			if array[j] == current_element:
				count += 1
			if count > ele_factor:
				return array[j]
	return None


# METHOD 2 (Using Binary Search Tree)
# when inserting increment the count whenever the count becomes more than n/2 then exit and return the element
class BST(object):
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.count = 1

def insert(root, data):
	if root == None:
		return BST(data)
	else:
		while







if __name__ == "__main__":
	array = [2,3,4,4,4,4,4]
	print find_majority_element(array)