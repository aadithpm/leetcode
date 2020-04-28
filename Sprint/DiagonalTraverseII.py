class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = collections.defaultdict(list)
        for idx, row in enumerate(nums):
            for j in range(len(row)):
                diagonals[idx + j].append(row[j])
        i, res = 0, []
        
        while i in diagonals:
            res.extend(diagonals[i][::-1])
            i += 1
        return res
