from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        return zip(*Counter(nums).most_common(k))[0]
        
        """
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        return sorted(counter, key = counter.get, reverse = True)[0:k]
        """
        