class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {
            'L': 0,
            'R': 0,
            'split': 0,
        }
        for letter in s:
            if counts['L'] == counts['R'] and counts['L'] > 0:
                counts['L'] = counts['R'] = 0
                counts['split'] += 1
            counts[letter] += 1
        return counts['split'] + 1 if counts['L'] == counts['R'] and counts['L'] > 0 else counts['split']
            
