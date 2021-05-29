"""

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, sum):
    if not root:
        return False

    stack = [(root, 0)]
    while stack:
        node, s = stack.pop()
        if not node.left and not node.right and s + node.val == sum:
            return True
        if node.left:
            stack.append((node.left, s + node.val))
        if node.right:
            stack.append((node.right, s + node.val))
    return False

def has_path(root, sum):
    if not root:
        return False

    def dfs(node, s):
        if not node:
            if s == sum:
                return True
            else:
                return False
        return dfs(node.left, s + node.val) or dfs(node.right, s + node.val)

    return dfs(root, 0)


def has_path(root, sum):
    if not root:
        return False
    if root.val == sum and not root.left and not root.right:
        return True
    return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
