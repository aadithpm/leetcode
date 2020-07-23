class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen = set()
        
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        
        return seen
