'''linked list to string'''

from preloaded import Node

def stringify(node):
    '''convert linked list to string'''
    lst=''
    while node is not None:
        lst+=str(node.data)+' -> '
        node = node.next

    lst+='None'
    return lst
