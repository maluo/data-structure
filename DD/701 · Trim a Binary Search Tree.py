"""
Description
Given the root of a binary search tree and 2 numbers min and max, trim the tree such that all the numbers in the new tree are between min and max (inclusive). The resulting tree should still be a valid binary search tree. So, if we get this tree as input:
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
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree 
    """
    def trimBST(self, root, minimum, maximum):
        # write your code here
        if root is None:
            return root
        
        if root.val < minimum:
            return self.trimBST(root.right, minimum, maximum)
        
        elif root.val > maximum:
            return self.trimBST(root.left, minimum, maximum)
        
        else:
            root.left = self.trimBST(root.left, minimum, maximum)
            root.right = self.trimBST(root.right, minimum, maximum)
        
        return root


