"""

 999 + 99999 


 9 -> 9 -> 9 
 9 -> 9 -> 9 -> 9 -> 9

 ---------------------
 8



None

8 -> None


prev_node = 8

9 -> 8 -> None


prev_node = 9

9 ->9 -> 8 -> None


"""

class LinkedNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None



def length(node):
	count = 0
	while node is not None:
		node = node.next
		count += 1

	return count


def sum_to_lists(head1, head2):
	l1 = length(head1)
	l2 = length(head2)

	if not l1:
		return l2

	if not l2:
		return l1

	r = 0
	prev_node = None
	while head1 is not None or head2 is not None:
		val1 = head1.val if head1 else 0
		val2 = head2.val if head2 else 0

		s = val1 + val2 + r
		if s >= 10:
			r = 1
			s = s % 10
		else:
			r = 0

		"""
		1.  8 -> None
		2. 9 -> 8 -> None
		3. 9 -> 9 -> 8 -> None
		4. 0 -> 9 -> 9 -> 8 -> None
		5. 0 -> 0 -> 9 -> 9 -> 8 -> None
		"""
		new_node = LinkedNode(s)  # 8
		new_node.next = prev_node # 8 -> None, 9 -> (8 -> None)
		prev_node = new_node

		head1 = head1.next if head1.next else None
		head2 = head2.next if head2.next else None

	if r > 0:
		# value exists at the end. edge cases for values like 999 + 1
		#  8 ->9 ->9 -> 0 -> 0 -> 1
		# node  = 1 -> 0 -> 0 -> 9 -> 9 -> 8 -> None
		node = LinkedNode(r)
		node.next = prev_node
		head = node
	else:
		head = prev_node
	
	return head












































