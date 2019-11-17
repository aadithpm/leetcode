def minimumHours(rows, columns, grid):
    def all_visited(matrix):
        for row in matrix:
            if 0 in row:
                return False
        return True

    def get_neighbors(i, j):
        neighbors = []
        
        if i - 1 > -1:
            neighbors.append((i - 1, j))
        if i + 1 < rows:
            neighbors.append((i + 1, j))
        if j - 1 > -1:
            neighbors.append((i, j - 1))
        if j + 1 < columns:
            neighbors.append((i, j + 1))
        
        return neighbors

    steps = 0
    while not all_visited(grid):
        steps += 1
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0:
                    neighbors = get_neighbors(i, j)
                    for pair in neighbors:
                        k, l = pair[0], pair[1]
                        if grid[k][l] == 1:
                            grid[i][j] = -1
                        
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == -1:
                    grid[i][j] = 1
    
    return steps
