"""
Description
Implement a function to check if a linked list is a palindrome.
"""


class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # write your code here
        if not head:
            return True
        middle = self.get_middle(head)
        reverse_list = self.reverse(middle.next)
        while reverse_list:
            if reverse_list.val != head.val:
                return False
            else:
                reverse_list = reverse_list.next
                head = head.next
        return True
        
    def get_middle(self, head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def reverse(self, head):
        prev = None 
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev