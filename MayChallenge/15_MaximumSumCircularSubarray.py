class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = 0
        max_sum, min_sum = -float('inf'), float('inf')
        cur_max, cur_min = 0, 0
        for num in A:
            cur_max = max(num, cur_max + num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
            total += num
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum
        
