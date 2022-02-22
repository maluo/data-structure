"""
Description
Given a sorted (increasing order) array, Convert it to a binary search tree with minimal height.

Divide and Conquer - 分治法
1.先从理论上解决大框架问题
2.再用实例测试参数调整
3.自底向上逆推法，验证参数正确性
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
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        if not A:
            return None
        mid = len(A) // 2
        root = TreeNode(A[mid])
        root.left = self.sortedArrayToBST(A[:mid])
        root.right = self.sortedArrayToBST(A[mid + 1:])
        return root

class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        return self.BST(A, 0, len(A)-1)
    
    def BST(self, A, start, end):
        if start > end:
            return None

        mid = (start + end) // 2

        left = self.BST(A, start, mid - 1)
        right = self.BST(A, mid + 1, end)

        root = TreeNode(A[mid])
        root.left = left
        root.right = right

        return root    