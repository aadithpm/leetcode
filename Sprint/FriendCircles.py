class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = set()
        groups = 0

        def dfs(pos):
            for idx, follower in enumerate(M[pos]):
                if follower and idx not in seen:
                    seen.add(idx)
                    dfs(idx)

        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                groups += 1

        return groups
