# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        inorder = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
        return inorder
