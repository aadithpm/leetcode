class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dominoes_count = 0
        sets = {}
        for pair in dominoes:
            this_set = frozenset(pair)
            if this_set in sets:
                dominoes_count += sets[this_set]
                sets[this_set] += 1
            else:
                sets[this_set] = 1
        return dominoes_count
