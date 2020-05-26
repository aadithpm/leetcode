class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sums = {0: -1}
        maxlen = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            if total not in sums:
                sums[total] = i
            if total - k in sums:
                maxlen = max(maxlen, i - sums[total - k])        
        return maxlen
