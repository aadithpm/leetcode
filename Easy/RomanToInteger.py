class Solution:
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        val = 0
        for i in range(0, len(s) - 1):   
            if roman[s[i]] < roman[s[i + 1]]:
                val -= roman[s[i]]
            else:
                val += roman[s[i]]
        return val + roman[s[-1]]