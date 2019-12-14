# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return
        res = []
        def dfs(root, val):
            if root.left:
                dfs(root.left, val + str(root.val) + ".")
            if root.right:
                dfs(root.right, val + str(root.val) + '.')
            if not root.left and not root.right:
                res.append(val + str(root.val))
        dfs(root, '')
        return ['->'.join(i.split('.')) for i in res]
