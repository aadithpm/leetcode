class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key = lambda x: (x[0]))
        prev = float('-inf')
        print(intervals)
        for interval in intervals:
            if interval[0] < prev:
                return False
            prev = interval[1]
        return True
