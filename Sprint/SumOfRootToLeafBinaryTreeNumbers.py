# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.bin_sum = 0
        
        def dfs(node, res):
            res += str(node.val)
            if node.left:
                dfs(node.left, res)
            if node.right:
                dfs(node.right, res)
            if not node.left and not node.right:
                self.bin_sum += int(res, 2)
        
        dfs(root, '')
        return self.bin_sum
