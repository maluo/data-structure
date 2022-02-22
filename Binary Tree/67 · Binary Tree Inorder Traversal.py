"""
Definition of TreeNode:
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        self.paths = []
        self.dfs (root)
        return self.paths
    
    def dfs(self,node):
        
        if not node:
            return
        
        self.dfs(node.left)

        self.paths.append(node.val)
        
        self.dfs(node.right)
