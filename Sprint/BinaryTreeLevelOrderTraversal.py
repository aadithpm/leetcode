# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack = []
        level = []
        stack.append(root)
        while stack:
            level.append([node.val for node in stack])
            this_level = []
            for node in stack:
                this_level.extend([node.left, node.right])
            stack = [leaf for leaf in this_level if leaf]
        return level
