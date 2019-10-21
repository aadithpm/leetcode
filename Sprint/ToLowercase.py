class Solution:
    def toLowerCase(self, str: str) -> str:
        return ''.join([chr(ord(i) + 32) if ord(i) in range(65, 91) else i for i in str])
