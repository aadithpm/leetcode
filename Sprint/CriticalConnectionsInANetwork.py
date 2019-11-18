from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for vertex in connections:
            graph[vertex[0]].append(vertex[1])
            graph[vertex[1]].append(vertex[0])
        
        dfn = [None for i in range(n)]
        low = dfn[:]
        
        cur, start, res, self.cur = 0, 0, [], 0
        
        def dfs(node, parent):
            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for vertex in graph[node]:
                    if not dfn[vertex]:
                        dfs(vertex, node)
                
                if parent is not None:
                    l = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                else:
                    l = min(low[i] for i in graph[node] + [low[node]])
                
                low[node] = l
                                                        
        dfs(0, None)
        
        for vertex in connections:
            if low[vertex[0]] > dfn[vertex[1]] or low[vertex[1]] > dfn[vertex[0]]:
                res.append(vertex)
        
        return res
