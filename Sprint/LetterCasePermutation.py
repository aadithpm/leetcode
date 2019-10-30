class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(subsets, idx, s):
            if idx == len(s):
                subsets.append(''.join(s))
            else:
                if s[idx].isalpha():
                    s[idx] = s[idx].upper()
                    backtrack(subsets, idx + 1, s)
                    s[idx] = s[idx].lower()
                    backtrack(subsets, idx + 1, s)
                else:
                    backtrack(subsets, idx + 1, s)
            
                    
        subsets = []
        backtrack(subsets, 0, list(S))
        return subsets
