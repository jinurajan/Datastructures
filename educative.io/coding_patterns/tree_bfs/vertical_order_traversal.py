"""
Find the vertical order traversal of a binary tree when the root of the binary tree is given. In other words, return the values of the nodes from top to bottom in each column, column by column from left to right. If there is more than one node in the same column and row, return the values from left to right.
"""


from collections import defaultdict, deque

# Tip: You may use some of the code templates provided
# in the support files

def vertical_order(root):
    if not root:
        return []
    node_list = defaultdict(list)
    min_level = 0
    max_level = 0

    q = [(root, 0)]
    while q:
        node, level = q.pop(0)
        if node:
            node_list[level].append(node.data)

            min_level = min(min_level, level)
            max_level = max(max_level, level)

            q.append((node.left, level-1))
            q.append((node.right, level+1))
    
    return [node_list[x] for x in range(min_level, max_level+1)]
