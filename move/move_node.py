'''move node from source chain to destination'''

class Node:
    '''class for Node'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Context:
    '''class for Context'''
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    '''func to move first node'''
    head = source.data
    source = source.next
    new_dest = Node(head)
    new_dest.next = dest
    return Context(source, new_dest)
