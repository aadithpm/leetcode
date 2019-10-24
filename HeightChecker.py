class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        hs = sorted(heights)
        count = 0
        for i, j in zip(heights, hs):
            if i != j:
                count += 1
        return count
