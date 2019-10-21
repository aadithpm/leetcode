# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        seq1, seq2 = [], []
        
        def get_leafs(root, seq):
            if not root.left and not root.right:
                seq.append(root.val)
            
            if root.left:
                get_leafs(root.left, seq)
            
            if root.right:
                get_leafs(root.right, seq)
            
            return seq
        
        return get_leafs(root1, seq1) == get_leafs(root2, seq2)
