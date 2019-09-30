class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = {}
        n_by_three = len(nums) // 3
        majority_elems = []
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for key, value in counts.items():
            if value > n_by_three:
                majority_elems.append(key)
        
        return majority_elems
