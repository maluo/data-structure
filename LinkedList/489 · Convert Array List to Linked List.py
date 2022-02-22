"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



class Solution:
    """
    @param: nums: an integer array
    @return: the first node of linked list
    """
    def toLinkedList(self, nums):
        dummy = ListNode(0) # dummy node points to head
        cur = dummy
        for num in nums:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next