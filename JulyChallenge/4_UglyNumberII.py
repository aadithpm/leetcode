class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        l2, l3, l5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[l2], 3 * ugly[l3], 5 * ugly[l5]
            umin = min((u2, u3, u5))
            if umin == u2:
                l2 += 1
            if umin == u3:
                l3 += 1
            if umin == u5:
                l5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
