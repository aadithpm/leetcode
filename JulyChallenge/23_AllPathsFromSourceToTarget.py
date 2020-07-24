class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        
        @lru_cache(maxsize=None)
        def search(node):
            if node == target:
                return [[target]]
            
            results = []
            for neighbor in graph[node]:
                for path in search(neighbor):
                    results.append([node] + path)
            
            return results
        
        return search(0)
