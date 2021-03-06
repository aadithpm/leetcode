# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not q and not p:
            return True

        if (not p and q) or (not q and p):
            return False
        
        return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
