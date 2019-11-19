from collections import defaultdict
def criticalConnections(connections):
        graph = defaultdict(list)
        for vertex in connections:
            graph[vertex[0]].append(vertex[1])
            graph[vertex[1]].append(vertex[0])
        
        n = len(graph)
        
        visited = [False] * n
        discovery = [float("inf")] * n
        low = discovery[:]
        parent = [-1] * n
        articulation = [False] * n
        res = []
        time = 0
        
        def dfs(node, time):
            children = 0
            visited[node] = True
            discovery[node] = time
            low[node] = time
            time += 1
            
            for vertex in graph[node]:
                if not visited[vertex]:
                    parent[vertex] = node
                    children += 1
                    dfs(vertex, time)
                    
                    low[node] = min(low[node], low[vertex])
                    
                    if parent[node] == -1 and children > 1:
                        articulation[node] = True
                    
                    if parent[node] != -1 and low[vertex] >= discovery[node]:
                        articulation[node] = True
                
                elif vertex != parent[node]:
                    low[node] = min(low[node], discovery[vertex])
            
        
        dfs(0, 0)
        
        for idx, val in enumerate(articulation):
            if val:
                res.append(idx)

        return res



#################

links = [[[0, 1], [1, 2], [0, 2], [2, 3], [2, 4], [3, 4]],
[[0, 1], [1, 2], [0, 2], [0, 3], [3, 4]],
[[0, 1], [1, 2], [2, 3]],
[[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]],
[[0, 1], [0, 2], [0, 3]]]

for link in links:
    print(criticalConnections(link))

