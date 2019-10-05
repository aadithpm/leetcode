class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        prev = 0
        total = 0
        for i in s[::-1]:
            this = numerals[i]
            if prev > this:
                total -= this
            else:
                total += this
            prev = this
        return total
