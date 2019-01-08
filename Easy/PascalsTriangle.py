class Solution:
    def generate(self, numRows):
        
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        tri = []
        for row in range(numRows):
            this_row = [None for i in range(row + 1)]
            this_row[0], this_row[-1] = 1, 1
            for i in range(1, len(this_row) - 1):
                this_row[i] = tri[row - 1][i - 1] + tri[row - 1][i]
            tri.append(this_row)
        return tri