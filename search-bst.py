#在solution class里面写function需要加self
#代表class本身
#方便共享variable和function
#参考angular的structure


# iteration
def searchBST(self, root, val):

    while root and root.val != val:
        if val < root.val:
            root = root.left
        else:
            root = root.right
    return root

# recursion
def searchBST_Recursion(self, root, val):
    if root is None or root.val == val:
        return root
    if val < root.val:
        return self.searchBST_Recursion(root.left, val)
    else:
        return self.searchBST_Recursion(root.right.val)

#