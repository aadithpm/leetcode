class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sums = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                target = nums[i] + nums[l] + nums[r]
                if target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
                else:
                    three_sums.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return three_sums
                
