from heapq import *
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(min(k, len(matrix))):
            heappush(heap, (matrix[i][0], 0, matrix[i]))
        
        count, number = 0, 0
        while heap:
            number, i, row = heappop(heap)
            count += 1
            if count == k:
                break
            if len(row) > i + 1:
                heappush(heap, (row[i + 1], i + 1, row))
        return number
