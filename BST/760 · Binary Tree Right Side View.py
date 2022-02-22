"""
Description
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom
"""

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def __init__(self):
        self.view = []

    def rightSideView(self, root):
        # write your code here  
        self.collect(root, 0)
        return self.view

    def collect(self,node,depth):
        if node:
            if depth == len(self.view):
                self.view.append(node.val)
            self.collect(node.right,depth + 1)
            self.collect(node.left,depth + 1)
