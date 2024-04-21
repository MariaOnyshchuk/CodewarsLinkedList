'''sort binary tree'''
def tree_by_levels(node):
    '''func which return list'''
    if not node:
        return []
    q = [node]
    lst = []
    while q:
        current = q.pop(0)
        lst.append(current.value)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return lst
