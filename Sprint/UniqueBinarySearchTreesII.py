
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        
        def gen(start, end):
            if start == end:
                return None
            result = []
            for i in range(start, end):
                for left in gen(start, i) or [None]:
                    for right in gen(i + 1, end) or [None]:
                        node = TreeNode(i)
                        node.left, node.right = left, right
                        result.append(node)
            return result
            
        return gen(1, n + 1)
