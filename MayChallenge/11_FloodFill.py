class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = set()
        def dfs(sr, sc, oldColor, newColor):
            if sr < len(image) and sr > -1 and sc < len(image[0]) and sc > -1 and image[sr][sc] == oldColor and (sr, sc) not in visited:
                visited.add((sr, sc))
                image[sr][sc] = newColor
                dfs(sr + 1, sc, oldColor, newColor)
                dfs(sr, sc + 1, oldColor, newColor)
                dfs(sr - 1, sc, oldColor, newColor)
                dfs(sr, sc - 1, oldColor, newColor)
        dfs(sr, sc, image[sr][sc], newColor)
        return image
        
