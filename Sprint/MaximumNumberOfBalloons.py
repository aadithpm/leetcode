from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        return min(Counter(text)[i] // Counter("balloon")[i] for i in Counter("balloon"))
        
        
            
