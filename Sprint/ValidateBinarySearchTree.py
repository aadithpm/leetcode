# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        
        def inorder(root, output):
            if not root:
                return None
            
            inorder(root.left, output)
            output.append(root.val)
            inorder(root.right, output)
            
        inorder(root, output)
        for i in range(1, len(output)):
            if output[i - 1] >= output[i]:
                return False
        
        return True
    
        
