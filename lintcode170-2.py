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
        def get_Length(self,head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length
        
        if head is None:
            return None
        
        dummy = ListNode(-1)
        dummy.next = head
        
        length = get_Length(head)
        k = k % length
        #basically length - k, just incase the k > length
        
        fast = dummy
        for i in range(k): #move to the cut point first with first pointer
            fast = fast.next
        
        slow = dummy
        while fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = dummy.next
        dummy.next = slow.next
        slow.next = None
        
        return dummy.next
        
        
    
   
    