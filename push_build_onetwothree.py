'''Linked Lists - Push & BuildOneTwoThree'''

from preloaded import Node

def push(head, data):
    '''push head'''
    node =  Node(data)
    if not head:
        return node
    node.next = head
    return node

def build_one_two_three():
    '''create linked list from 1 to 3'''
    head = None
    for i in range(3, 0, -1):
        head = push(head, i)

    return head
