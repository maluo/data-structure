"""
# 公理,作图观察得,无法推理：
# In a recursion with boolean return type, once there is a level returning false, all false.
#
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
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    枚举三种不同的情况，到达叶子借点，仅其中一个是null，两个借点值不相等
    """
    def isIdentical(self, a, b):
        # write your code here
        if a == None and b == None:
            return True
        
        if a == None or b == None:
            return False

        if a.val != b.val: # once return false, then the result will be false, only need once
            return False

        a1 = self.isIdentical(a.left, b.left)
        b1 = self.isIdentical(a.right,b.right) # once there is a level returning false, all false?

        return a1 and b1