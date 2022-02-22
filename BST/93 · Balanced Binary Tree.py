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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        
        if not self.isBalanced(root.left):
            return False
        
        if not self.isBalanced(root.right):
            return False
        
        return abs(self.get_height(root.left) - self.get_height((root.right))) <= 1


    def get_height(self,root):
        if not root:
            return 0
        return max(self.get_height(root.left), self.get_height(root.right)) + 1