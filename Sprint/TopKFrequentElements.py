from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        return [i[0] for i in sorted(counts.items(), key = lambda x: x[1], reverse=True)[:k]]
