from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_matrix = defaultdict(list)
        indegree = {}
        
        for dest, src in prerequisites:
            adj_matrix[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        
        zero_degrees = deque([i for i in range(numCourses) if i not in indegree])
        topological = []
        
        while zero_degrees:
            vertex = zero_degrees.popleft()
            topological.append(vertex)
            
            if vertex in adj_matrix:
                for neighbor in adj_matrix[vertex]:
                    indegree[neighbor] -= 1
                    
                    if indegree[neighbor] == 0:
                        zero_degrees.append(neighbor)
        
        return topological if len(topological) == numCourses else []
