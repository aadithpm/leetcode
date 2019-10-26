class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator / denominator)
        
        res = ''
        if numerator / denominator < 0:
            res += '-'
            numerator = abs(numerator)
            denominator = abs(denominator)
        
        res += str(numerator / denominator) + '.'
        
        numerator %= denominator
        i = len(res)
        remainder = {}
        while numerator != 0:
            if numerator not in remainder:
                remainder[numerator] = i
            else:
                i = remainder[numerator]
                res = res[:i] + "(" + res[i:] + ")"
                return res
            
            numerator *= 10
            res += str(numerator / denominator)
            numerator %= denominator
            i += 1
        return res
