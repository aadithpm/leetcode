# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        nodes = []
        def inorder(root, nodes):
            if not root:
                return
            inorder(root.left, nodes)
            nodes.append(root.val)
            inorder(root.right, nodes)
        inorder(root, nodes)
        l, r = 0, len(nodes) - 1
        while l < r:
            temp = nodes[l] + nodes[r]
            if temp == k:
                return True
            if temp < k:
                l += 1
            else:
                r -= 1
        return False
