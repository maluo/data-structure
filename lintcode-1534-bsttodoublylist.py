class Solution:
    def __init__(self):
        self.first = None
        self.prev = None
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        if root is None:
            return None
        
        head, tail = self.dfs(root)
        
        # 因为题目要求是环，所以还要首尾相连
        tail.right = head
        head.left = tail
        
        return head
        
    def dfs(self, root):
        if root is None:
            return None, None
            
        left_head, left_tail = self.dfs(root.left)
        right_head, right_tail = self.dfs(root.right)
        
        # left tail <-> root
        if left_tail:
            left_tail.right = root
            root.left = left_tail
        # root <-> right head
        if right_head:
            root.right = right_head
            right_head.left = root
        
        # 其实 root 肯定是有的，第三个 or 只是为了好看
        head = left_head or root or right_head
        tail = right_tail or root or left_tail
        
        return head, tail