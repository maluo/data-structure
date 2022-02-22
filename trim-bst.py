def trimBST(self, root, min, max):
    if root is None:
        return None

    root_val = root.val

    # root value betwen range
    if min <= root_val and root_val <= max:
        root.left = self.trimBST(root.left, min, root_val)
        root.right = self.trimBST(root.right, root_val, max)
        return root

    # root value < min, trim left
    elif root_val < min:
        return self.trimBST(root.right, min, max)

    # root value > max, trim right
    else:
        return self.trimBST(root.left, min, max)
