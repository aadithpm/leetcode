from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        max_so_far = 0
        
        for key in counts:
            if key + 1 in counts:
                max_so_far = max(max_so_far, counts[key] + counts[key + 1])
    
        return max_so_far
