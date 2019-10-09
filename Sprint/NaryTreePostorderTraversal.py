"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = []
        elems = []
        
        stack.append(root)
        while stack:
            root = stack.pop()
            elems.append(root.val)
            for i in range(0, len(root.children)):
                stack.append(root.children[i])
        
        return elems[::-1]
