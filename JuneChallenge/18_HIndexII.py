  class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations) - 1
        while l <= r:
            m = l + (r - l) // 2
            if citations[m] == len(citations) - m:
                return citations[m]
            elif citations[m] > len(citations) - m:
                r = m - 1
            else:
                l = m + 1
        return len(citations) - (r + 1)
