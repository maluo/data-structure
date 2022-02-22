"""
Description
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

get_height(): 先猜想，后作图验证。
练习倒推法的好例子，通过root,left,right,三个简单的模式先找到规律 max(left,right) + 1,再通过调用相同函数作图验证
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