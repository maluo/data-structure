"""
Description
Given a linked list and two values v1 and v2. Swap the two nodes in the linked list with values v1 and v2. It's guaranteed there is no duplicate values in the linked list. If v1 or v2 does not exist in the given linked list, do nothing.
"""

"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        #find preV1 and preV2
        #swap (preV1.next, preV2.next) then swap (preV1.next.next, preV2.next.next)
        dummy = ListNode(0, head)
        preV1 = dummy
        preV2 = dummy
        while preV1.next and preV1.next.val != v1:
            preV1 = preV1.next
        if not preV1.next:
            return dummy.next
        while preV2.next and preV2.next.val != v2:
            preV2 = preV2.next
        if not preV2.next:
            return dummy.next
        preV1.next, preV2.next = preV2.next, preV1.next
        preV1.next.next, preV2.next.next = preV2.next.next, preV1.next.next
        return dummy.next