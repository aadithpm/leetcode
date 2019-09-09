class Solution:
    def maxArea(self, height: List[int]) -> int:
        fp, sp = 0, len(height) - 1
        maxarea = 0
        while fp < sp:
            area = min(height[fp], height[sp]) * (sp - fp)
            maxarea = max(maxarea, area)
            if height[fp] < height[sp]:
                fp += 1
            else:
                sp -= 1
        return maxarea
