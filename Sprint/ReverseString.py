class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        h = len(s) - 1
        while l < h:
            temp = s[l]
            s[l] = s[h]
            s[h] = temp
            l += 1
            h -= 1
