"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + self.depth(root)
    
    def depth(self, root):
        if root and root.children:
            return 1 + max([self.depth(child) for child in root.children])
        else:
            return 0