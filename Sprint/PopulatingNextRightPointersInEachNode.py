"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        queue = collections.deque([root])
        orig_root = root
        while queue:
            level = queue
            queue = collections.deque([])
            while level:
                candidate = level.popleft()
                if level and level[0]:
                    candidate.next = level[0]
                else:
                    candidate.next = None

                if candidate.left:
                    queue.append(candidate.left)
                if candidate.right:
                    queue.append(candidate.right)

        return orig_root
