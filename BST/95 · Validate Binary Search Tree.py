"""
Description
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
"""

"""
Definition of TreeNode:
"""
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        MAX = sys.maxsize
        MIN = -sys.maxsize-1
        return self.validate(root, MAX, MIN)

    def validate(self, node, _max, _min):
        if node is None:
            return True
        
        if node.val >= _max or node.val <= _min:
            return False
        
        return self.validate(node.left, node.val, _min) and self.validate(node.right, _max, node.val)
