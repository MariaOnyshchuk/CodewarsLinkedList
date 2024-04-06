'''week 9'''

class Node:
    '''class of Nodes for linked list'''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    '''convert string to linked list'''
    lst = s.split(' -> ')[::-1]
    if lst.pop(0) == 'None':
        prev_node = None
    if not lst:
        return None
    while lst:
        curr_node = Node(int(lst.pop(0)), prev_node)
        prev_node = curr_node
    return curr_node
