# Input : {3,9,20,#,#,15,7}
# Output: [[3],[20,9],[15,7]]
# ZigZag 锯齿形
# Practice on BFS with Queue

# Bonus:
# Practice on BFS with Stack later 

import collections

class Solution:

    def TreeNode (self,val):
        return

    def zigzagLevelOrder(self, root: TreeNode):
        lists = []
        if not root:
            return lists
        q = collections.deque() #clear queue
        left_to_right = True
        q.append(root)

        while len(q) != 0:
            size = len(q)
            l = [] # current level
            for i in range(size):
                node = q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                l.reverse()
            lists.append(l)
            left_to_right = not left_to_right
        return lists