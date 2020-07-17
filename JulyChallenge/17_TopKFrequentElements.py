class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}
        
        for num in nums:
            if num in buckets:
                buckets[num] += 1
            else:
                buckets[num] = 1
    
        tuples = sorted(buckets.items(), key=lambda x: x[1], reverse=True)[:k]
        res = []
        for val in tuples:
            res.append(val[0])

        return res
