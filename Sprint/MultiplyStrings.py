class Solution:
    def _int(self, num: str) -> int:
        inum = 0
        for i in range(len(num)):
            inum += (ord(num[i]) - 48) * 10 ** (len(num) - i - 1)
        return inum
    
    def _str(self, num: int) -> str:
        if num == 0:
            return "0"
        
        snum = ''
        while num > 0:
            snum += chr(48 + num  % 10)
            num //= 10
        return snum[::-1]

    def multiply(self, num1: str, num2: str) -> str:
        return self._str(self._int(num1) * self._int(num2))
