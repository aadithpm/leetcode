class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        per_min, per_hour = 6, 30
        
        _minutes = per_min * minutes
        hours = (hour % 12 + minutes / 60) * per_hour
        
        return min(abs(hours - _minutes), 360 - abs(hours - _minutes))
