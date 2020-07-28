class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = collections.Counter(tasks)
        fmax = max(freqs.values())
        nmax = list(freqs.values()).count(fmax)
        return max(len(tasks), (fmax - 1) * (n + 1) + nmax)
