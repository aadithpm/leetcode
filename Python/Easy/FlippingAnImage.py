class Solution(object):
    
    def invert(self, elem):
        return 1 if elem == 0 else 0

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        image = []
        for row in A:
            image.append([self.invert(i) for i in row[::-1]])
        return image
