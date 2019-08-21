class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        all_nums = []
        for row in matrix:
            all_nums.extend(row)
        all_nums = list(sorted(all_nums))
        return all_nums[k - 1]