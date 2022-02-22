"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# 本质上，用递归的方式，实现了穷举
# exit point, 回归方程，传值以及复用
# function exits directly, not returning values to the top

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root:
            return []
        results = []
        self.dfs(root, target, [root.val], results)
        return results
    
    def dfs(self, root, target, path, results):
        print(path)
        if not root.left and not root.right:
            if sum(path) == target:
                results.append(path[:])
            return
        if root.left:
            self.dfs(root.left, target, path+[root.left.val], results)
        if root.right:
            self.dfs(root.right, target, path+[root.right.val], results)