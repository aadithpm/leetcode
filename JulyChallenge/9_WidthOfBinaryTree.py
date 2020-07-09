class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_width = 0
        queue = collections.deque([(0, root)])

        while queue:
            this_length = len(queue)
            idx, level = queue[0]
            
            for i in range(this_length):
                col_idx, node = queue.popleft()
                if node.left:
                    queue.append((2 * col_idx, node.left))
                if node.right:
                    queue.append((2 * col_idx + 1, node.right))
            
            max_width = max(max_width, col_idx - idx + 1)
        
        return max_width
