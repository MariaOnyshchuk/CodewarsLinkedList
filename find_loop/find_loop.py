'''loop'''

def loop_size(node):
    '''count length of loop'''
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            i = 0
            while i==0 or slow != fast:
                slow = slow.next
                i+=1
            return i
    return None
