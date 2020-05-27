class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for pair in dislikes:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
            
        colors = [-1] * (N)
        colors[0] = 1
        seen = set()
        
        def bfs(v):
            queue = collections.deque()
            queue.append(v)
            while queue:
                vertex = queue.pop()
                for i in range(1, N + 1):
                    if i in graph[vertex] and colors[i - 1] == -1:
                        colors[i - 1] = 1 - colors[vertex - 1]
                        seen.add(i)
                        queue.append(i)
                    elif i in graph[vertex] and colors[i - 1] == colors[vertex - 1]:
                        return False
            return True

        for i in range(1, N - 1):
            if i not in seen:
                seen.add(i)
                if not bfs(i):
                    return False
        return True
