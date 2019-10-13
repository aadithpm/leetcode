class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = set()
        count = 0
        
        for letter in s:
            if letter in letters:
                count += 1
                letters.remove(letter)
            else:
                letters.add(letter)
        
        if len(letters) > 0:
            return count*2 + 1
        else:
            return count*2
