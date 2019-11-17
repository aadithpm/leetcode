class NumArray:

    def __init__(self, nums: List[int]):
        if nums:
            s = [0] * len(nums)
            s[0] = nums[0]
            for i in range(1, len(nums)):
                s[i] = s[i - 1] + nums[i]

            self.s = s
        
    def sumRange(self, i: int, j: int) -> int:
        if not self.s:
            return
        if i == 0:
            return self.s[j]
        return self.s[j] - self.s[i-1]
