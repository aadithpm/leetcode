class Solution:
    def create_mapping(self):
        letters = 'abcdefghijklmnopqrtuvwxy'
        mapping, j, k = {}, 0, 3
        for i in range(2, 10):
            mapping[str(i)] = list(letters[j:k])
            j, k = k, k + 3
        mapping['7'].append('s')
        mapping['9'].append('z')
        
        return mapping
    
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        mapping = self.create_mapping()
        
        if len(digits) == 1:
            return mapping[digits[0]]
        
        subsets = []
        
        def backtrack(subsets, letters, idx, digits):
            if len(letters) == len(digits):
                subsets.append(''.join(letters))
            else:
                for letter in mapping[digits[idx]]:
                    letters.append(letter)
                    backtrack(subsets, letters, idx + 1, digits)
                    letters.pop()
        
        backtrack(subsets, [], 0, digits)
        return subsets
