class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, length, res = sorted(nums), len(nums), []
        for i in range(length):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, length - 1
                while l < r:
                    total = nums[l] + nums[r] + nums[i]
                    if total < 0 or (l > i + 1 and nums[l] == nums[l - 1]):
                        l += 1
                    elif total > 0 or (r < length - 1 and nums[r] == nums[r + 1]):
                        r -= 1
                    else:
                        res.append([nums[l], nums[r], nums[i]])
                        l += 1
                        r -= 1
        return res
