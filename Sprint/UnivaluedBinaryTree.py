# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(root, uni):
            if not root:
                return True
            return root.val == uni and dfs(root.left, uni) and dfs(root.right, uni)
        return dfs(root, root.val)
