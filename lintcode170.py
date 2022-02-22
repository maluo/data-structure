class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """

    def rotateRight(self, head, k):
        # write your code here
        if head == None:
            return None

        # record the length of linked list
        p = head
        length = 0
        while p:
            length += 1
            p = p.next
        k = k % length

        dummy = ListNode(None, head)
        pre = dummy
        for i in range(k):
            pre = dummy.next

            while pre.next.next:
                pre = pre.next  # locate pre every time

            tmp = pre.next
            tmp.next = head
            head = tmp
            pre.next = None
            dummy.next = tmp

        return head
