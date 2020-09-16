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
	if not head1:
		return l2

	if not head2:
		return l1

	r = 0
	prev_node = None
	while head1.next is not None or head2.next is not None:
		val1 = head1.val if head1 else 0
		val2 = head2.val if head2 else 0

		s = val1 + val2 + r
		if s >= 10:
			r = 1
			s = s % 10

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
		if head1.next:
			head1 = head1.next
		if head2.next:
			head2 = head2.next
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



def print_ll(node):
	while node is not None:
		print node.val,
		node = node.next

head1 = LinkedNode(9)
head1.next = LinkedNode(9)
head1.next.next = LinkedNode(9)

head2 = LinkedNode(9)
head2.next = LinkedNode(9)
head2.next.next = LinkedNode(9)
head2.next.next.next = LinkedNode(9)
head2.next.next.next.next = LinkedNode(9)

r = sum_to_lists(head1, head2)

print_ll(r)











































