# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(idx, lower, upper):
            if self.idx == len(preorder) or preorder[self.idx] < lower or preorder[self.idx] > upper:
                return None
            root = TreeNode(preorder[self.idx])
            self.idx += 1
            root.left = dfs(self.idx, lower, root.val)
            root.right = dfs(self.idx, root.val, upper)
            return root
        self.idx = 0
        return dfs(0, float('-inf'), float('inf'))
