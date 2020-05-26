class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {}
        maxlen, count = 0, 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                maxlen = max(maxlen, i + 1)

            if count in counts:
                maxlen = max(maxlen, i - counts[count])
            else:
                counts[count] = i
        
        return maxlen
