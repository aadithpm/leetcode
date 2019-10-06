class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid: List[List[str]], i: int, j: int):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1' or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(grid, i + 1, j)
            dfs(grid, i - 1, j)
            dfs(grid, i, j + 1)
            dfs(grid, i, j - 1)
        
        count = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(grid, i, j)
                    count += 1
        return count
