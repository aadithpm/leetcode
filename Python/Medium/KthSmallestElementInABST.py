# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nodes = []
        while root or nodes:
            while root:
                nodes.append(root)
                root = root.left
            root = nodes.pop()
            k = k - 1
            if k == 0:
                return root.val
            root = root.right