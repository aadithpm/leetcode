class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        visit = [0 for i in range(numCourses)]
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
        
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            
            visit[i] = -1
            for course in graph[i]:
                if not dfs(course):
                    return False
            
            visit[i] = 1
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
