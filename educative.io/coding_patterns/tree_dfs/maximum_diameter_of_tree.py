"""

"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeDiameter:

    def find_diameter(self, root):
        max_dia = float("-inf")

        def dfs(node):
            nonlocal max_dia
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            l_dia = max(dfs(node.left), 0)
            r_dia = max(dfs(node.right), 0)
            max_dia = max(max_dia, l_dia + r_dia + 1)
            return max(l_dia, r_dia) + 1

        dfs(root)
        return max_dia




def main():
    treeDiameter = TreeDiameter()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
    root.left.left = None
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    root.right.left.right.left = TreeNode(10)
    root.right.right.left.left = TreeNode(11)
    print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()







