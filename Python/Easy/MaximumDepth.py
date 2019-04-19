class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            lh = self.maxDepth(root.left)
            rh = self.maxDepth(root.right)
            return max(lh, rh) + 1