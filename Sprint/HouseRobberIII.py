# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.rob_sub(root))
    
    def rob_sub(self, root):
        if root is None:
            return [0, 0]
        left = self.rob_sub(root.left)
        right = self.rob_sub(root.right)
        res = [0, 0]
        
        res[0] = max(left) + max(right)
        res[1] = root.val + left[0] + right[0]
        
        return res
