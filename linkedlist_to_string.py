class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    lst=''
    while node!=None:
        lst+=str(node.data)+' -> '
        node = node.next
        
    lst+='None'
    return lst
