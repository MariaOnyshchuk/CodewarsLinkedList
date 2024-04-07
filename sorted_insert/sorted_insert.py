'''insert node correctly'''

class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def sorted_insert(head, data):
    if head is None:
        return Node(data)
    current = head
    if head.data>data:
        head = Node(data)
        head.next = current
        return head
    while current.data < data:
        if current.next is None:
            current.next = Node(data)
            return head
        current = current.next
    now = Node(current.data)
    now.next = current.next
    current.data = data
    current.next = now

    return head
