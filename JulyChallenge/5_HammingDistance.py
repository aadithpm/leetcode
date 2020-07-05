class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        bits = 0
        
        while xor > 0:
            bits += xor & 1
            xor >>= 1
        
        return bits
