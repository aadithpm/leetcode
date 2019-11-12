class Solution:
    def checkRecord(self, s: str) -> bool:
        a = False
        for i in range(0, len(s)):
            if s[i] == 'A':
                if a:
                    return False
                a = True
            if i < len(s) - 1 and s[i : i + 3] == 'LLL':
                return False
        return True
