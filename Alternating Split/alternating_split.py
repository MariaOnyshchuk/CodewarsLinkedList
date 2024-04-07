'''split into two chains'''

class Node(object):
    '''node class'''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    '''for 2 chains'''
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    '''split chain into two'''
    if not head or not head.next:
        raise TypeError
    current = head
    first_chain = Node(current.data)
    f = first_chain
    second_chain = Node(current.next.data)
    s = second_chain
    current = current.next.next
    i=3
    while current:
        if i%2!=0:
            f.next = Node(current.data)
            f = f.next
        else:
            s.next = Node(current.data)
            s = s.next
        current = current.next
        i+=1

    return Context(first_chain, second_chain)
