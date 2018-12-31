class Solution:
    def majorityElement(self, nums):
        counts = {}
        # counts = collections.Counter(nums)
        for i in nums:
            if i in counts: counts[i] += 1
            else: counts[i] = 1
        return max(counts, key = counts.get)
        