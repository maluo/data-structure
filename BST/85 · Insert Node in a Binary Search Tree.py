"""
Description
Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.
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
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        return self._helper(root, node)
        

    def _helper(self,root,node):

        if  root is None:
            return node
        
        if node.val < root.val:
            root.left = self._helper(root.left, node)
        
        else:
            root.right = self._helper(root.right, node)
        
        return root