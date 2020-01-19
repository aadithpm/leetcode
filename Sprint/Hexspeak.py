class Solution:
    def toHexspeak(self, num: str) -> str:
        valid = {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O', '1', '0'}
        conv = hex(int(num))[2:].upper()
        for c in conv:
            if c not in valid:
                return 'ERROR'
        conv = conv.replace('0', 'O').replace('1', 'I')
        return conv
