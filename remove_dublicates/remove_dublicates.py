class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None or head.next is None:
        return head
    new = head
    while new and new.data and new.next:
        if new.data == new.next.data:
            new.next = new.next.next
        else:
            new = new.next
    return head

def linked_list_from_string(s):
    '''convert string to linked list'''
    lst = s.split(' -> ')[::-1]
    if lst.pop(0) == 'None':
        prev_node = None
    if not lst:
        return None
    while lst:
        curr_node = Node(int(lst.pop(0)))
        curr_node.next = prev_node
        prev_node = curr_node
    return curr_node

def stringify(node):
    '''convert linked list to string'''
    lst=''
    while node is not None:
        lst+=str(node.data)+' -> '
        node = node.next

    lst+='None'
    return lst

print(stringify(remove_duplicates(linked_list_from_string('1 -> 1 -> 1 -> 1 -> 1 -> 1 -> None'))))