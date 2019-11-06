class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, h = 0, n - 1
        while l < h:
            mid = (l + h) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
        rotations = l
        l, h = 0, n - 1
        while l <= h:
            mid = (l + h) // 2
            r_mid = (mid + rotations) % n
            if nums[r_mid] == target:
                return r_mid
            if nums[r_mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return -1
