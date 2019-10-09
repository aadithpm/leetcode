"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        elems = []
        
        stack.append(root)
        while stack:
            root = stack.pop()
            elems.append(root.val)
            for i in range(len(root.children) - 1, -1, -1):
                stack.append(root.children[i])
        
        return elems
