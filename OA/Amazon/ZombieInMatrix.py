from collections import deque
def zombie_matrix(grid):
    if not grid:
        return 0

    humans = 0
    r, c = len(grid), len(grid[0])
    queue = deque([])
    
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                queue.append((i, j))
            else:
                humans += 1
    
    if humans == 0:
        return humans
    
    temp_count = 0
    dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    while queue:
        temp_count += 1
        for i in range(len(queue)):
            i, j = queue.popleft()
            for x, y in dirs:
                rx = i + x
                ry = j + y
                if rx < 0 or ry < 0 or rx >= r or ry >= c or grid[rx][ry] == 1:
                    continue
                grid[rx][ry] = 1
                humans -= 1
                if humans == 0:
                    return temp_count
                queue.append((rx, ry))
    
    return -1

