"""
This Question is from facebook How to Interview from facebook
You are given a binary tree find the average of values in each depth


"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def __collect_1(node, data, depth=0):
    if not node:
        return None
    if depth not in data:
        data[depth] = []
    data[depth].append(node.val)
    __collect_1(node.left, data, depth+1)
    __collect_1(node.right, data, depth+1)


def avg_by_depth_1(node):
    data = {}
    __collect_1(node, data)
    result = []
    for i in range(len(data)):
        result.append(sum(data[i]) / i if i > 0 else sum(data[i]))
    return result


def __collect(node, data, depth=0):
    if not node:
        return None
    if depth not in data:
        data[depth] = (node.val, 1)
    else:
        data[depth][0] += node.val
        data[depth][1] += 1
    __collect(node.left, data, depth+1)
    __collect(node.right, data, depth+1)


def avg_by_depth(node):
    data = {}
    __collect(node, data)
    result = []
    for i in range(len(data)):
        val, count = data[i]
        result.append(val / count)
    return result
