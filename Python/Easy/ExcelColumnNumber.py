class Solution:
    def titleToNumber(self, s):
        n = len(s)
        column_num = 0
        for idx, val in enumerate(s):
            column_num += (ord(val) - 65 + 1) * 26 ** (n - idx - 1)
        return column_num