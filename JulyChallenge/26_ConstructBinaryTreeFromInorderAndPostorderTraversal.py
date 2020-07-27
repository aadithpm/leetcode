# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inord_map = {k: v for v, k in enumerate(inorder)}
        def build_tree(l, r):
            if l <= r:
                root = TreeNode(postorder.pop())
                mid = inord_map[root.val]
                root.right = build_tree(mid + 1, r)
                root.left = build_tree(l, mid - 1)
                return root
        return build_tree(0, len(inorder) - 1)
