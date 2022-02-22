class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        newNode = ListNode(val)

        if head is None: #no elements
            return newNode

        elif val <= head.val: #insert to head
            newNode.next = head
            return newNode

        else:
            node = head
            
            while node.next:
                #most important logic
                if node.val < val and val <= node.next.val:
                    newNode.next = node.next
                    node.next = newNode
                    return head
                node = node.next

            node.next = newNode # if dropping into the last element
            return head