"""
Maximum XOR of Two Numbers in an Array

Given a non empty array of numbers a0, a1, a2 .... an-1 where 0 <= ai < 2 raised to 31

Find the maximum result of ai ^ aj where 0 <=i j < n

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

"""

class SolutionBF(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_xor = 0
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] ^ nums[j] > max_xor:
                    max_xor = nums[i] ^ nums[j]

        return max_xor


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            found = set([num & mask for num in nums])
            start = ans | 1 << i
            for prefix in found:
                if start ^ prefix in found:
                    ans = start
                    break
        return ans




class TrieNode(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val



def print_trie(root):
    if not root:
        print ""
        return 
    print_trie(root.left)
    print_trie(root.right)
    print root.val,


def insert(root, num):
    curr = root
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        if bit == 0:
            if not curr.left:
                curr.left = TrieNode(bit)
            curr = curr.left
        else:
            if not curr.right:
                curr.right = TrieNode(bit)
            curr = curr.right



class SolutionTrie(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        trie_head = TrieNode()
        for num in nums:
            insert(trie_head, num)
        max_xor = 0
        for i in range(len(nums)):
            value = nums[i]
            curr = trie_head
            curr_xor = 0 
            for j in range(31, -1, -1):
                b = (value >> j ) & 1
                if b == 0:
                    # go to the right
                    if curr.right:
                        curr_xor += pow(2, j)
                        curr = curr.right
                    else:
                        curr = curr.left
                else:
                    # try to go to left
                    if curr.left:
                        curr_xor += pow(2, j)
                        curr = curr.left
                    else:
                        curr = curr.right
            if curr_xor > max_xor:
                max_xor = curr_xor
        return max_xor



print SolutionBF().findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
print SolutionBF().findMaximumXOR([4, 6, 7 ]) == 3
print SolutionBF().findMaximumXOR([14,15,9,3,2]) == 13

print Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
print Solution().findMaximumXOR([4, 6, 7 ]) == 3
print Solution().findMaximumXOR([14,15,9,3,2]) == 13

print SolutionTrie().findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
print SolutionTrie().findMaximumXOR([4, 6, 7 ]) == 3
print SolutionTrie().findMaximumXOR([14,15,9,3,2]) == 13






