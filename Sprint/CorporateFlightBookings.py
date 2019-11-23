class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        # TLE
        total = {i: 0 for i in range(1, n + 1)}
        for start, end, count in bookings:
            for i in range(start, end + 1):
                total[i] = total[i] + count
        return [booking[1] for booking in sorted(total.items(), key = lambda x: x[0])]
        """
        res = [0] * n
        for start, end, count in bookings:
            res[start - 1] += count
            if end < n:
                res[end] -= count
        for i in range(1, n):
            res[i] += res[i - 1]
        return res
