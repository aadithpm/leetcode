class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        def area(r, c):
            if not (len(grid) > r >= 0 and len(grid[0]) > c >= 0 and (r, c) not in seen
                   and grid[r][c] == 1):
                return 0
            seen.add((r, c))
            return (1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1))

        areas = [area(r, c) for r in range(len(grid)) for c in range(len(grid[0]))]
        return max(areas)
