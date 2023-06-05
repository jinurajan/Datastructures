"""
A thief has discovered a new neighborhood to target, where the houses can be represented as nodes in a binary tree. The money in the house is the data of the respective node. The thief can enter the neighborhood from a house represented as root of the binary tree. Each house has only one parent house. The thief knows that if he robs two houses that are directly connected, the police will be notified. The thief wants to know the maximum amount of money he can steal from the houses without getting caught by the police. The thief needs your help determining the maximum amount of money he can rob without alerting the police.

The number of nodes in the tree is in the range[1, pow(10,4)]

0 <= node.data >= pow(10,4)
"""


from collections import *

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        # below data members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = 0


class BinaryTree:
    # constructor
    def __init__(self, *args):
        if len(args) < 1:
            self.root = None
        elif isinstance(args[0], int):
            self.root = BinaryTreeNode(args[0])
        else:
            self.root = None
            self.insertList(args[0])

    # function to create the binary tree given a list of integers
    def insertList(self, inputList):
        if not inputList:
            self.root = None
        else:
            self.root = BinaryTreeNode(inputList[0])
            q = deque([self.root])
            i = 1
            while i < len(inputList):
                currentNode = q.popleft()
                if inputList[i] != None:
                    currentNode.left = BinaryTreeNode(inputList[i])
                    q.append(currentNode.left)
                i += 1
                if i < len(inputList) and inputList[i] != None:
                    currentNode.right = BinaryTreeNode(inputList[i])
                    q.append(currentNode.right)
                i += 1

    # function to find a node given the value stored in the node
    def find(self, value):
        q = deque([self.root])
        while q:
            currentNode = q.popleft()
            if currentNode:
                if currentNode.data == value:
                    return currentNode
                q.append(currentNode.left)
                q.append(currentNode.right)
            if all(val == None for val in q):
                break
        return None

    # function to return level order traversal of the binary tree
    def level_order_traversal(self):
        if not self.root:
            return []
        result = []
        q = deque([self.root])
        while q:
            currentNode = q.popleft()
            if currentNode:
                result.append(currentNode.data)
                q.append(currentNode.left)
                q.append(currentNode.right)
            else:
                result.append(None)
            if all(val == None for val in q):
                break
        return result


def rob(root):
    def heist(node):
        if not node:
            return [0,0]
        l_tree= heist(node.left)
        r_tree = heist(node.right)
        root_included = node.data + l_tree[1] + r_tree[1]
        exclude_root = max(l_tree)+max(r_tree)
        return [root_included, exclude_root]
    
    return max(heist(root))

    
    

def main():
    input1 = [10, 9, 20, 15, 7]
    tree1 = BinaryTree(input1)

    input2 = [7, 9, 10, 15, 20]
    tree2 = BinaryTree(input2)

    input3 = [8, 2, 17, 1, 4, 19, 5]
    tree3 = BinaryTree(input3)

    input4 = [7, 3, 4, 1, 3]
    tree4 = BinaryTree(input4)

    input5 = [9, 5, 7, 1, 3]
    tree5 = BinaryTree(input5)


    inputTrees = [tree1.root, tree2.root, tree3.root, tree4.root, tree5.root]
    x = 1
    for i in inputTrees:
        print(x, ".\tInput Tree:", sep = "")
        display_tree(i)
        x+=1
        print("\tMaximum amount we can rob without getting caught: ", rob(i), sep = "")
        print("-" * 100)

if __name__ == "__main__":
    main()

    
