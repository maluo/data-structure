# Check if t2 is sub-tree of t1

def isSubTree(self, t1, t2):

    # Edge case
    if t2 is None:
        return True

    if t1 is None:
        return False

    # 先序处理了根节点
    if self.is_equal(t1, t2):
        return True

    return self.isSubTree(t1.left, t2) or self.isSubTree(t1.right, t2)


def is_equal(self, t1, t2):
    
    # if True, then all the levels in the recursion does not trigger t1.val != t2.val
    # values are all the same
    if t1 is None and t2 is None:
        return True

    # makes the return value as false
    if t1 is None or t2 is None:
        return False

    if t1.val != t2.val:
        return False

    return self.is_equal(t1.left, t2.left) and self.is_equal(t1.right, t2.right)
