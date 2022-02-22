"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # write your code here
        if a == None and b == None:
            return True
        
        # Node or structure match    
        if a == None or b == None:
            return False 
        
        # Value match
        if a.val != b.val:
            return False
        
        a1 = self.isIdentical(a.left, b.left)
        b1 = self.isIdentical(a.right, b.right)
        
        return a1 and b1