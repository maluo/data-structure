"""
Description
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Input:  {1,#,2,3}
Output: 3	
Explanation:
	1
	 \ 
	  2
	 /
	3    
it will be serialized {1,#,2,3}
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
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        self.minLevel = 0
        self.dfs(root, 1)
        return self.minLevel

    def dfs(self,node,curLevel):
        if not node:
            return
        
        self.minLevel = min(curLevel,self.minLevel)
        self.dfs(node.left,curLevel + 1)
        self.dfs(node.right,curLevel + 1)



"""
1. 画图注意分层
2. 在最下面的子节点一探一回式
3. 看图例理解后两个判定条件
4. 自底向上的设计思路
关注点：
1.DFS数据结构 - 本质是前序便利
2.自底向上设计思路
3.设计时候注意分层看待返回结果
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if root.left and root.right:
            return min(leftDepth, rightDepth) + 1
        else:
            return max(leftDepth, rightDepth) + 1