from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        r, c = len(grid), len(grid[0])
        queue = deque([])
        
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if not count:
            return count
        
        temp_count = 0
        dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        
        while queue:
            temp_count += 1
            for i in range(len(queue)):
                x, y = queue.popleft()
                for cx, cy in dirs:
                    rx = x + cx
                    ry = y + cy
                    if rx < 0 or ry < 0 or rx >= r or ry >= c or grid[rx][ry] != 1:
                        continue
                    grid[rx][ry] = 2
                    queue.append((rx, ry))
                    count -= 1
        
        return temp_count - 1 if count == 0 else -1
