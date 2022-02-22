# Find Leaves of Binary Tree
# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.
# 逐层砍树，最后为空

# DFS
# Pre-order
# Mid-order
# Post-order

class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class DFS:
    
    def findLeaves(self, root):
        lists = []
        self.dsf(root, lists)
        return lists

    def dfs(self, node, lists):
        if node is None:
            return -1

        left = self.dfs(node.left, lists)
        right = self.dfs(node.right, lists)

        cur = max(left, right) + 1
        self.add_into_lists(lists, cur, node.val)
        return cur

    def add_into_lists(self, lists, level, value):
        if level == len(lists):
            lists.append([])
        lists[level].append(value)