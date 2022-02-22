class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """

    def __init__(self):
        self.first, self.last = None, None

    # build an iterator so that we can flattern the tree to get a increasing order
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            # iterate the tree like a list
            if self.first is None:
                self.first = node
            if self.prev:
                self.last.right = node
                node.left = self.last
            self.last = node

            self.inorder(node.right)

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
