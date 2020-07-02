# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = collections.deque()
        queue = collections.deque([root])
        while queue:
            level = []
            nodes = []
            while queue:
                nodes.append(queue.popleft())
            for node in nodes:
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.appendleft(level)
        return res
