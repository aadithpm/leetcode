class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)
        offset = 1
        for i in range(1, num + 1):
            if(offset * 2 == i):
                offset *= 2
            res[i] = res[i - offset] + 1
        return res
        
