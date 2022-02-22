"""
DFS - preorder

1. break point

2. carry over value

3. traverse left and right
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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        self.depth = 0
        self.dfs(root, 1)
        return self.depth
        
    def dfs(self,node,curdepth):
        if not node:
            return
        self.depth = max(self.depth,curdepth)
        self.dfs(node.left, curdepth + 1)
        self.dfs(node.right, curdepth + 1)
