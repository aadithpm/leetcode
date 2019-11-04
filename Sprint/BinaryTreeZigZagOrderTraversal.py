# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]: 
        if not root:
            return []
        ans, level, zigzag = [], [root], 1
        while level:
            ans.append([node.val for node in level[::zigzag]])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
            zigzag *= -1
        return ans
