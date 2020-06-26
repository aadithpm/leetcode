# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        def dfs(root, seq):
            if not root.left and not root.right:
                res.append(int(seq + str(root.val)))
            if root.left:
                dfs(root.left, seq + str(root.val))
            if root.right:
                dfs(root.right, seq + str(root.val))
        dfs(root, '')
        return sum(res)
