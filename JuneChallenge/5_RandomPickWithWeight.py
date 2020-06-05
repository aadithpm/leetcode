import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefixes = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefixes.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        l, h = 0, len(self.prefixes)
        while l < h:
            m = l + (h - l) // 2
            if target > self.prefixes[m]:
                l = m + 1
            else:
                h = m
        return l
