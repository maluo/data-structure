class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        # write your code here
        self.num = 0
        self.dfs(root)
        return self.num
        
    def dfs(self, root):
        
        if root is None:
            return 
        
        if root.left is None and root.right is None:
            self.num += root.val
        
        self.dfs(root.left)
        self.dfs(root.right)