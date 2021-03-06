class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        tuples = {}
        for a in A:
            for b in B:
                if a + b in tuples:
                    tuples[a + b] += 1
                else:
                    tuples[a + b] = 1
        count = 0
        for c in C:
            for d in D:
                if -c - d in tuples:
                    count += tuples[-c - d]
        return count