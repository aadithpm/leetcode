class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        shift = 0
        l = len(arr)
        zeroes = arr.count(0)
        for i in range(l - 1, -1, -1):
            if i + zeroes < l:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < l:
                    arr[i + zeroes] = 0
        
