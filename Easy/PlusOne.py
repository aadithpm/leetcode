class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        """
        integer = 0
        for idx, val in enumerate(digits):
            integer = integer + (val * pow(10, (len(digits) - 1 - idx)))  
        return [int(i) for i in str(integer + 1)]
        """
        
        number = int(('').join([str(i) for i in digits]))
        return [int(i) for i in str(number + 1)]