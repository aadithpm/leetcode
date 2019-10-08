class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1] * i for i in range(1, rowIndex + 2)]
        for i in range(2, rowIndex + 1):
            for j in range(1, len(triangle[i]) - 1):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle[rowIndex]
