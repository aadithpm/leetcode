class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.res = 0
        roads = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, parent):
            if (parent, node) in roads:
                self.res += 1
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
        dfs(0, -1)
        return self.res
