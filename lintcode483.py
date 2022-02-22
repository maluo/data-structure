class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the head of linked list.
    @return: An integer list
    """
    def toArrayList(self, head):
        # write your code here
        node = head
        lst = []
        while node is not None:
            lst.append(node.val)
            node = node.next
        return lst
            

        