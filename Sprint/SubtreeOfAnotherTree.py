# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
# Merkle hashing:

class Solution:
    def isSubtree(self, s, t):
        def merkle(node):
            if not node:
                return '#'
            left_hash = merkle(node.left)
            right_hash = merkle(node.right)
            node.merkle = '#' + ' ' + left_hash + ' ' + str(node.val) + ' ' + right_hash
            return node.merkle

        merkle(s)
        merkle(t)

        def dfs(node):
            if not node:
                return False
            return node.merkle == t.merkle or (dfs(node.left) or dfs(node.right))

        return dfs(s)
        
"""

class Solution:
    def same(self, s, t):
            if not s and not t:
                return True
            if (s and not t) or (t and not s):
                return False
            return s.val == t.val and self.same(s.left, t.left) and self.same(s.right, t.right)


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.same(s, t):
            return True
        if not s:
            return False
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
