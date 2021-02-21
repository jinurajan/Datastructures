"""
Lowest Common Ancestor of a Binary Tree III
Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q exist in the tree.

"""



"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution1:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if p.parent == q.parent:
            return p.parent
        p_stack = [p]
        q_stack = [q]
        p_parent = p
        q_parent = q
        while p_stack and q_stack:
            node_p = p_stack.pop()
            node_q = q_stack.pop()
            if node_p == node_q:
                return p.parent
            if node_q == node_p:
                return q.parent
            if p_parent.left:
                p_stack.append(p_parent.left)
            if p_parent.right:
                p_stack.append(p_parent.right)
            if q_parent.left:
                q_stack.append(q_parent.left)
            if q_parent.right:
                q_stack.append(q_parent.right)
        if p_stack:
            return p.parent.val
        if q_stack:
            return q.parent.val


class Solution1:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if p.parent == q.parent:
            return p.parent
        if p.parent == q:
            return q
        if q.parent == p:
            return p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = p.parent
        while q not in ancestors:
            q = q.parent
        return q


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent_map = {}
        while p:
            parent_map[p] = True
            p = p.parent
        while q:
            if q in parent_map:
                return q
            q = q.parent

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            if p1.parent:
                p1 = p1.parent
            else:
                p1 = q
            if p2.parent:
                p2 = p2.parent
            else:
                p2 = p
        return p1

root = Node(3)
root.left = Node(5)
root.left.parent = root
root.right = Node(1)
root.right.parent = root
root.left.left = Node(6)
root.left.left.parent = root.left
root.left.right = Node(2)
root.left.right.parent = root.left
root.left.right.left = Node(7)
root.left.right.left.parent = root.left.right
root.left.right.right = Node(4)
root.left.right.right.parent = root.left.right

root.right.left = Node(0)
root.right.left.parent = root.right
root.right.right = Node(8)
root.right.right.parent = root.right

# print(Solution().lowestCommonAncestor(root.left, root.left.right.right).val)
# print(Solution().lowestCommonAncestor(root.left, root.right).val)
# print(Solution().lowestCommonAncestor(root.left.left, root.right.right).val)
# print(Solution().lowestCommonAncestor(root.left.right.left, root.left.right.right).val)

root = Node(1)
root.left = Node(2)
root.left.parent = root
import pdb; pdb.set_trace()
print(Solution().lowestCommonAncestor(root, root.left).val)