# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
        if root is None:
            return tail
        
        x = TreeNode(root.val)
        x.right = self.increasingBST(root.right, tail)
        return self.increasingBST(root.left, x)
