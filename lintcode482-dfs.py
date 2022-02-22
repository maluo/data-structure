class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def levelSum(self, root, level):
        # write your code here
        lists = []
        # anomaly detection
        if not root:
            return 0
        self.dfs(root, 0, lists)
        # anomaly detection
        if level > len(lists) or level <= 0:
            return 0
        return sum(lists[level - 1])

    def dfs(self, root, cur_level, lists):
        if not root:
            return
        # create a list for storing the elements of the current level
        if cur_level == len(lists):
            lists.append([])
        lists[cur_level].append(root.val)
        self.dfs(root.left, cur_level + 1, lists)
        self.dfs(root.right, cur_level + 1, lists)