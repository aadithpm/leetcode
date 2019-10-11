"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[int]:
        q = [root] if root else []
        elems = []
        while q:
            elems.append([n.val for n in q])
            q = [child for n in q for child in n.children if n]
        return elems
