class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, point in enumerate(stations):
            print(dp)
            for j in range(i, -1, -1):
                if dp[j] >= point[0]:
                    dp[j + 1] = max(dp[j + 1], dp[j] + point[1])
        
        for idx, dist in enumerate(dp):
            if dist >= target:
                return idx
        
        return -1
