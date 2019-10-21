# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append([root, 1])
        while queue:
            node, depth = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return depth
                queue.append([node.left, depth + 1])
                queue.append([node.right, depth + 1])
