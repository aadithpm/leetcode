import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = queue.Queue()
        q.put(root)
        q.put(root)
        
        while q.empty() is False:
            n1 = q.get()
            n2 = q.get()
            
            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None:
                return False
            if n1.val != n2.val:
                return False
            
            q.put(n1.left)
            q.put(n2.right)
            q.put(n1.right)
            q.put(n2.left)
            
        return True