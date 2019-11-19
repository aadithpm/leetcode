class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return
        res = []
        
        def backtrack(s, temp, res):
            if not s or len(s) == 0:
                res.append(temp[:])
                return
            for i in range(1, len(s) + 1):
                substr = s[0:i]
                if substr != substr[::-1]:
                    continue
                temp.append(substr)
                backtrack(s[i:], temp, res)
                temp.pop()
                
        
        backtrack(s, [], res)
        return res
    
