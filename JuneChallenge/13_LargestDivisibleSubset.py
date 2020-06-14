class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @lru_cache(maxsize=None)
        def eds(i):
            tail = nums[i]
            max_subset = []
            for n in range(0, i):
                if tail % nums[n] == 0:
                    subset = eds(n)
                    if len(max_subset) < len(subset):
                        max_subset = subset
            max_subset = max_subset.copy()
            max_subset.append(tail)
            return max_subset

        if len(nums) == 0:
            return []
        nums.sort()
        return max([eds(i) for i in range(len(nums))], key=len)
