class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num_logs = []
        let_logs = []
        for log in logs:
            if log.split(' ')[1].isdigit():
                num_logs.append(log)
            else:
                let_logs.append(log)
        let_logs.sort(key=lambda x: x.split()[0])
        let_logs.sort(key=lambda x: x.split()[1:])
        return let_logs + num_logs
