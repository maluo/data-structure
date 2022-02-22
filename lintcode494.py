class Stack:
    def __init__(self):
        self.queue_a = collections.deque()
        self.queue_b = collections.deque()
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.queue_a.append(x)
        while self.queue_b:
            self.queue_a.append(self.queue_b.popleft())
        self.queue_a, self.queue_b = self.queue_b, self.queue_a
        

    """
    @return: nothing
    """
    def pop(self):
        if self.queue_b:
            self.queue_b.popleft()
    """
    @return: An integer
    """
    def top(self):
        if self.queue_b:
            return self.queue_b[0]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return not self.queue_b