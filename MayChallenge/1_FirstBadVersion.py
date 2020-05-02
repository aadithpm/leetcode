def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid):
                if mid == 1:
                    return mid
                if isBadVersion(mid):
                    r = mid - 1
                else:
                    return mid
            else:
                l = mid + 1
        return l
