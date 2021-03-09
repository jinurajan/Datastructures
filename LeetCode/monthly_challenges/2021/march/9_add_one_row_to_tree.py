"""
Add One Row to Tree
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:

Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

Example 2:
Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
        depth = 1
        queue = deque([(root, depth)])
        while depth < d:
            size = len(queue)
            while size:
                node, depth = queue.popleft()
                if depth + 1  == d:
                    # we have to insert new nodes here
                    if not node.left and not node.right:
                        # leaf node
                        node.left = TreeNode(v)
                        node.right = TreeNode(v)
                    else:
                        if node.left:
                            old_left = node.left
                            new_node = TreeNode(v)
                            node.left = new_node
                            new_node.left = old_left
                        else:
                            node.left = TreeNode(v)
                        if node.right:
                            old_right = node.right
                            new_node = TreeNode(v)
                            node.right = new_node
                            new_node.right = old_right
                        else:
                            node.right = TreeNode(v)
                if node:
                    if node.left:
                        queue.append((node.left, depth+1))
                    if node.right:
                        queue.append((node.right, depth+1))
                size -= 1
        return root

class Solution1:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        depth = 1
        queue = [root]
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            root = new_root
        while depth < d:
            if depth + 1 == d:
                for i in range(len(queue)):
                    new_l_node = TreeNode(v)
                    new_r_node = TreeNode(v)
                    if queue[i].left:
                        left = queue[i].left
                    else:
                        left = None
                    if queue[i].right:
                        right = queue[i].right
                    else:
                        right = None
                    queue[i].left = new_l_node
                    queue[i].right = new_r_node
                    new_l_node.left = left
                    new_r_node.right = right
                break
            q = []
            while queue:
                node = queue.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            queue = q
            depth += 1
        return root



class Solution2:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        depth = 1
        queue = [root]
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            root = new_root
        while depth < d:
            if depth + 1 == d:
                for i in range(len(queue)):
                    new_l_node = TreeNode(v)
                    new_r_node = TreeNode(v)
                    if queue[i].left:
                        left = queue[i].left
                    else:
                        left = None
                    if queue[i].right:
                        right = queue[i].right
                    else:
                        right = None
                    queue[i].left = new_l_node
                    queue[i].right = new_r_node
                    new_l_node.left = left
                    new_r_node.right = right
                break
            q = []
            while queue:
                node = queue.pop()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            queue = q
            depth += 1
        return root


from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """ Using dfs ie recursion stack"""
        if d == 1:
            return TreeNode(v, left=root)

        def dfs(node, v, d, depth):
            if depth + 1  == d:
                left_tree = TreeNode(v, left=node.left)
                right_tree = TreeNode(v, right=node.right)
                node.left = left_tree
                node.right = right_tree
                return
            if node.left:
                dfs(node.left, v, d, depth+1)
            if node.right:
                dfs(node.right, v, d, depth+1)
        dfs(root, v, d, 1)
        return root



def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.val, end=" ")
    inorder_traversal(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

new_root = Solution().addOneRow(root, 5, 4)
inorder_traversal(new_root)
print("*********")
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)
new_root = Solution().addOneRow(root, 1, 2)
inorder_traversal(new_root)

print("****")
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)
new_root = Solution().addOneRow(root, 1, 3)
inorder_traversal(new_root)



