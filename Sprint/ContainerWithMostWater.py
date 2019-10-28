class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxarea = 0
        while l < r:
            length = r - l
            area = min(height[l], height[r]) * length
            maxarea = max(maxarea, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea
