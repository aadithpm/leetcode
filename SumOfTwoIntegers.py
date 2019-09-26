class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0: return b
        if b == 0: return a
        mask = 0xffffffff
        
        while b != 0:
            c = a & b
            a = (a ^ b) & mask
            b = (c << 1) & mask
        
        if a >> 31 & 1:
            return ~(a ^ mask)
        
        return a
