# Binary Tree Maximum Path Sum

class Solution:

    def __init__(self):
        
        self.max_sum = float('-inf')

    def maxPathSum(self, root):
        
        if root is None:
            return 0

        self.get_max_path_sum(root)
        
        return self.max_sum

    def get_max_path_sum(self, node):
        
        if node is None:
            return 0

        max_left = self.get_max_path_sum(node.left)
        max_right = self.get_max_path_sum(node.right)

        self.max_sum = max(self.max_sum, max_left+max_right+node.val)
        current_max = node.val + max(max_left, max_right)

        return current_max if current_max > 0 else 0