class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        l, h = 0, 10**8
        while h - l > 1e-6:
            mid = float((l + h) / 2)
            dist = sum(int((stations[i + 1] - stations[i]) / mid) for i in range(len(stations) - 1))
            if dist <= K:
                h = mid
            else:
                l = mid
        return l
