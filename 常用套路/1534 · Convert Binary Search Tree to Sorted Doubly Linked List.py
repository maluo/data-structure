"""
Description
Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
"""

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:

    def __init__(self):
        self.first, self.last = None, None
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
       # Write your code here.
        if not root:
            return root
        self.first = None
        self.last = None
        self.inorder(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            # iterate the tree like a list
            if self.first is None:
                self.first = node
            if self.last:
                self.last.right = node
                node.left = self.last
            self.last = node

            self.inorder(node.right)