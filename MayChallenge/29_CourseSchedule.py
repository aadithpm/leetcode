class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for i in range(numCourses)]
        degrees = [0] * numCourses
        for course, prereq in prerequisites:
            edges[prereq].append(course)
            degrees[course] += 1
        queue = collections.deque(idx for idx, degree in enumerate(degrees) if degree == 0)
        while queue:
            course = queue.popleft()
            for edge in edges[course]:
                degrees[edge] -= 1
                if not degrees[edge]:
                    queue.append(edge)
        return not sum(degrees)
