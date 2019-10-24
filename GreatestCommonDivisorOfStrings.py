class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)
        g = gcd(len(str1), len(str2))
        return str1[:g] if str1[:g] * (len(str2) // g) == str2 and str2[:g] * (len(str1) // g) == str1 else ''
