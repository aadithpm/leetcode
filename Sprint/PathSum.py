
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        
        def dfs(root, sum):
            if not root:
                return False
            if not root.left and not root.right and root.val == sum:
                return True
            
            sum -= root.val
            return dfs(root.left, sum) or dfs(root.right, sum)
        
        return dfs(root, sum)
