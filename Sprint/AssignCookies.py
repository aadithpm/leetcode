class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        
        count = 0
        cookie = 0
        
        while cookie < len(s) and count < len(g):
            if s[cookie] >= g[count]:
                count += 1
            cookie += 1 
            
        return count
