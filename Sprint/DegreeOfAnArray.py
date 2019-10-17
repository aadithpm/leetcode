class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        res = len(nums)
        for idx, num in enumerate(nums):
            if num not in counts:
                counts[num] = [idx, idx, 1]
            else:
                counts[num] = [min(counts[num][0], idx), max(counts[num][1], idx), counts[num][2] + 1]
        degree = max(counts.values(), key=lambda x: x[2])[2]
        for entry in counts:
            if counts[entry][2] == degree:
                res = min(res, counts[entry][1] - counts[entry][0] + 1)
        return res
