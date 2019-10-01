from collections import OrderedDict
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False
        
        buckets = OrderedDict()
        
        for num in nums:
            key = num if not t else num // t
            for m in (buckets.get(key - 1), buckets.get(key), buckets.get(key + 1)):
                if m is not None and abs(num - m) <= t:
                    return True
            
            if len(buckets) == k:
                buckets.popitem(False)
            buckets[key] = num
            
        return False
