"""
Description
Given a binary tree, return all root-to-leaf paths.

Input：{1,2,3,#,5}
Output：["1->2->5","1->3"]
Explanation：
   1
 /   \
2     3
 \
  5
"""

"""
Learn:
Learn the join operation
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):

        if not root:
            return []
        # write your code here
        self.paths = []
        self.dfs(root,[root])
        return self.paths
    
    def dfs(self,node,path):

        if node is None:
            return

        if not node.left and not node.right:
            self.paths.append('->'.join([str(n.val) for n in path]))
            return
        
        path.append(node.left)
        self.dfs(node.left,path)
        path.pop() # pop the last item, most likely null

        path.append(node.right)
        self.dfs(node.right, path)
        path.pop()
