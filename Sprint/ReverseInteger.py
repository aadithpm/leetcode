class Solution:
    def reverse(self, x: int) -> int:
        minus = x < 0
        x = abs(x)
        new_num = 0
        while x > 0:
            new_num = (new_num * 10) + x % 10
            x //= 10
            
        if new_num > 0x7FFFFFFF:
            return 0
        
        return new_num * -1 if minus else new_num
