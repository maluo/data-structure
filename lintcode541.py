class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        from collections import deque
        self.q = deque([])
        self.total_count = 0
        for a in vecs:
            if a:
                self.total_count += len(a)
                self.q.appendleft(a[::-1])
        
    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        lst = self.q.pop()
        ret = lst.pop()
        self.total_count -= 1
        if lst:
            self.q.appendleft(lst)
        return ret

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return self.total_count > 0