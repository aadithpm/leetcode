from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return []
        level = 0
        queue = deque([root, ])
        while queue:
            levels.append([])
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        
        zigzag = []
        for idx, row in enumerate(levels):
            if idx % 2 == 0:
                zigzag.append(row)
            else:
                zigzag.append(row[::-1])
        return zigzag
