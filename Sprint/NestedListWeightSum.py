
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            res = 0
            for nestedint in nestedList:
                if nestedint.isInteger():
                    res += nestedint.getInteger() * depth
                else:
                    res += dfs(nestedint.getList(), depth + 1)
            return res
        return dfs(nestedList, 1)
