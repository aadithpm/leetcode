class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        timesheet = {}
        for idx, times in enumerate(zip(startTime, endTime)):
            start, end = times[0], times[1]
            for i in range(start, end + 1):
                if i in timesheet:
                    timesheet[i].append(idx)
                else:
                    timesheet[i] = [idx]
        return len(timesheet[queryTime]) if queryTime in timesheet else 0
