class Node():
    '''class of Nodes for linked list'''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    '''convert linked list to string'''
    lst=''
    while node is not None:
        lst+=str(node.data)+' -> '
        node = node.next

    lst+='None'
    return lst
