class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
        return -1 * heap[0]
        
