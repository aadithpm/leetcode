# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_map = {k: v for v, k in enumerate(inorder)}
        def build_tree(l, h):
            if l <= h:
                root = TreeNode(postorder.pop())
                mid = inorder_map[root.val]
                root.right = build_tree(mid + 1, h)
                root.left = build_tree(l, mid - 1)
                return root
        return build_tree(0, len(inorder) - 1)
