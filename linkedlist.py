# Build linked list and CRUDTraverse

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, location):
        cur = self.head
        for i in range(location):
            cur = cur.next
        return cur.next


def buildLinkedList():
    print("Build")
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    return node_1


def printLinkedList(node: ListNode):
    while node is not None:
        print(node.val, end=' ')
        node = node.next
    print("\n")


printLinkedList(buildLinkedList())
