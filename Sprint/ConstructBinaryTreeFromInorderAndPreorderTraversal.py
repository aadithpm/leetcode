from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        def build_tree(preorder, inorder):
            if inorder:
                r_idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[r_idx])
                root.left = build_tree(preorder, inorder[:r_idx])
                root.right = build_tree(preorder, inorder[r_idx + 1:])
                return root
        return build_tree(preorder, inorder)
