# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return None
        if root.val>key:
            root.left = self.deleteNode(root.left, key)
        if root.val<key:
            root.right = self.deleteNode(root.right, key)
        if root.val == key:
            if root.right and root.left:
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
            elif root.left:
                return root.left
            elif root.right:
                return root.right
            else:
                return None
        return root
