"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def levelSum(self, root, level):
        # write your code here
        if not root:
            return 0
            
        current_level = 0 
        stack = [root]
        
        while stack:
            node_values, new_stack = [], []
            for i in range(len(stack)):
                node = stack.pop()
                node_values.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            stack = new_stack
            current_level += 1 
            
            if current_level == level:
                return sum(node_values)
            
        return 0