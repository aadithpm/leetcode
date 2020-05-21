class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = {}
        max_len = 0
        for i in range(1, n + 1):
            total = sum(int(j) for j in str(i))
            if total in counts:
                counts[total].append(i)
            else:
                counts[total] = [i]
            max_len = max(max_len, len(counts[total]))
        return len([i for i in counts.values() if len(i) == max_len])
