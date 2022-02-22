class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyQueue:
    def __init__(self):
        self.before_head = ListNode(-1)
        self.tail = self.before_head
    
    """
    @param: item: An integer
    @return: nothing
    """
    def enqueue(self, item):
        self.tail.next = ListNode(item)
        self.tail = self.tail.next
        # write your code here
        return

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.before_head.next is None:
            return -1
        head_val = self.before_head.next.val
        self.before_head  = self.before_head.next
        return head_val
