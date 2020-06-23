# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_depth(self, root: TreeNode) -> int:
        depth = 0
        while root.left:
            root = root.left
            depth += 1
        return depth

    def exists(self, idx: int, depth: int, node: TreeNode) -> bool:
        l, r = 0, (2 ** depth) - 1
        for i in range(depth):
            m = l + (r - l) // 2
            if idx <= m:
                node = node.left
                r = m
            else:
                node = node.right
                l = m + 1
        return node is not None
    
    
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = self.get_depth(root)
        if depth == 0:
            return 1
        
        l, r = 1, (2 ** depth) - 1
        while l <= r:
            m = l + (r - l) // 2
            if self.exists(m, depth, root):
                l = m + 1
            else:
                r = m - 1
                
        return (2 ** depth - 1) + l
