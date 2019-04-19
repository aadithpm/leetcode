# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def traverse(self, root, inorder):
        if root:
            if root.left != None:
                self.traverse(root.left, inorder)
            inorder.append(root.val)
            if root.right != None:
                self.traverse(root.right, inorder)
        else:
            return []
        return inorder
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder = []
        return self.traverse(root, inorder)
        