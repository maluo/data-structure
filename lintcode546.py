class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class InterfaceQueue:
    def push(self, element):
        pass

    # define an interface for pop 
    # write your code here
    def pop(self):
        pass

    # define an interface for top method
    # write your code here
    def top(self):
        pass

class MyQueue(InterfaceQueue):
    # you can declare your private attributes here
    def __init__(self):
        # do initialization if necessary
        self.before_head = ListNode(-1)
        self.tail = self.before_head

        
    # implement the push method
    # write your code here
    def push(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
		
    # implement the pop method
    # write your code here
    def pop(self):
        if self.before_head.next is None:
            return -1
        else:
            val = self.before_head.next.val
            self.before_head = self.before_head.next
        return val
    	
	# implement the top method
    # write your code here
    def top(self):
        return self.before_head.next.val

        
# Your MyQueue object will be instantiated and called as such:
# MyQueue queue = new MyQueue();
# queue.push(123);
# queue.top(); will return 123;
# queue.pop(); will return 123 and pop the first element in the queue