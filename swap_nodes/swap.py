'''swap pairs of nodes'''
class Node:
    '''class Node'''
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    '''swap pairs'''
    if not head or not head.next:
        return head
    current = head
    new_start = current.next
    while head and head.next:
        first=current.next
        temp = first.next
        first.next = current
        if temp is None:
            current.next = None
            break
        if temp.next is None:
            current.next = temp
            break
        current.next = temp.next
        current=temp

    return new_start

(swap_pairs(Node(Node(Node(Node())))))