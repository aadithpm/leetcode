# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        output = []
        def inorder(root, output):
            if not root:
                return
            inorder(root.left, output)
            output.append(root.val)
            inorder(root.right, output)
        inorder(root, output)
        return output[k - 1]
