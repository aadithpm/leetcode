class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        lo, hi = 0, len(S)
        res = []
        for s in S:
            if s == 'I':
                res.append(lo)
                lo += 1
            else:
                res.append(hi)
                hi -= 1
        return res + [lo]
