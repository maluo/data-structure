"""
Definition of ListNode
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The first node of linked list.
    @return: Head node.
    """
    def removeDuplicates(self, head):
        # write your code here
        dummy = ListNode(-1,head)
        slow, fast = dummy, head
        visited = set()
        while fast:
            if fast.val not in visited:
                slow.next = fast
                slow = slow.next
                visited.add(fast.val)
            fast = fast.next
        slow.next = None
        return dummy.next

            