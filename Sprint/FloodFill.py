class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        start_pixel = image[sr][sc]
        
        if start_pixel == newColor:
            return image
        
        def helper(image, sr, sc, newColor):
            if image[sr][sc] == start_pixel:
                image[sr][sc] = newColor
                if sr < len(image) - 1:
                    helper(image, sr + 1, sc, newColor)
                if sr > 0:
                    helper(image, sr - 1, sc, newColor)
                if sc < len(image[0]) - 1:
                    helper(image, sr, sc + 1, newColor)
                if sc > 0:
                    helper(image, sr, sc - 1, newColor)
            return image
        
        return helper(image, sr, sc, newColor)
