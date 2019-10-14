class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        
        l, r = 0, num
        while l < r:
            mid = l + ((r - l) // 2)
            if mid * mid == num:
                return True
            elif num < mid * mid:
                r = mid
            else:
                l = mid + 1
        return False
