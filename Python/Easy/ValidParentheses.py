class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        symbols = []
        for i in s:
            if i in matches.keys():
                symbols.append(matches[i])
            elif i in matches.values():
                if len(symbols) < 1 or i != symbols.pop():
                    return False
        return len(symbols) == 0
                
                