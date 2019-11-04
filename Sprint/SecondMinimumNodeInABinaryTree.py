# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min1 = root.val
        self.ans = float('inf')

        def dfs(root):
            if root:
                if min1 < root.val < self.ans:
                    self.ans = root.val
                elif root.val == min1:
                    dfs(root.left)
                    dfs(root.right)
        
        dfs(root)
        return self.ans if self.ans < float('inf') else -1
