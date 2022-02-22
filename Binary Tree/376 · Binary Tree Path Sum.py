"""
sum(arr) -> get the sum of an array
"""

"""
Description
Given a binary tree, find all paths that sum of the nodes in the path equals to a given number target.

A valid path is from root node to any of the leaf nodes
"""

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

"""
Traverse all elements and keep appending on the result set
"""

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
        
        self.results = []
        
        self.dfs(root,target,[root.val])
        
        return self.results
    
    def dfs(self,root,target,path):

        # break condition
        if not root.left and not root.right:
            if sum(path) == target:
                self.results.append(path[:]) # append all
            return
        
        if root.left:
            self.dfs(root.left,target,path+[root.left.val])

        if root.right:
            self.dfs(root.right,target,path+[root.right.val])