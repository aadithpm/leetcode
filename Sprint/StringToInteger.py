class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        s = re.match(r'[-+]?\d+', str)
        try:
            result = int(s.group())
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0
