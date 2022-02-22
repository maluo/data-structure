"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
        
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        self.sum_leaves = 0;
        # write your code here
        if root is None:
            return 0
        self.dfs(root)
        return self.sum_leaves


    def dfs(self,root):
        if root is None:
            return

        if not root.left and not root.right:
            self.sum_leaves += root.val
        
        
        self.dfs(root.left)
        self.dfs(root.right)
