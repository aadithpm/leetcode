class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Stupid one pass solution
        places = {}
        res = len(s) + 1
        
        for idx, letter in enumerate(s):
            if letter not in places:
                places[letter] = idx
            else:
                places[letter] = '#'
        
        for letter in places:
            if places[letter] != '#':
                res = min(res, places[letter])
        
        return res if res < len(s) else -1
            
