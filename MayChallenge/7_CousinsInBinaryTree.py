class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([(root, None)])
        x_p, y_p = None, None
        while queue:
            for i in range(len(queue)):
                node, parent = queue.popleft()
                if node.val == x:
                    x_p = parent
                if node.val == y:
                    y_p = parent
                
                if node.left:
                    queue += [(node.left, node)]
                if node.right:
                    queue += [(node.right, node)]
                
            if x_p or y_p:
                if x_p and y_p and x_p is not y_p:
                    return True
                return False
        return False
