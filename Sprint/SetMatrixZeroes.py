class Solution(object):   
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        height, width = len(matrix), len(matrix[0])
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 0:
                    temp = j
                    while temp > -1:
                        if matrix[i][temp] != 0:
                            matrix[i][temp] = '-'
                        temp -= 1
                    temp = j
                    while temp < width:
                        if matrix[i][temp] != 0:
                            matrix[i][temp] = '-'
                        temp += 1

                    temp = i
                    while temp > -1:
                        if matrix[temp][j] != 0:
                            matrix[temp][j] = '-'
                        temp -= 1
                    temp = i
                    while temp < height:
                        if matrix[temp][j] != 0:
                            matrix[temp][j] = '-'
                        temp += 1

        for i in range(height):
            for j in range(width):
                if matrix[i][j] == '-':
                    matrix[i][j] = 0
