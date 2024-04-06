'''get node data by index'''

class Node():
    '''class of Nodes for linked list'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def get_nth(node, index):
    '''get node data'''
    if index<0:
        raise IndexError("Invalid index value should throw error.")
    if node is None:
        raise TypeError("None linked list should throw error.")
    for _ in range(index+1):
        if node is None:
            raise TypeError("Invalid index value should throw error.")
        curr_node = node
        node = node.next
    return curr_node
  