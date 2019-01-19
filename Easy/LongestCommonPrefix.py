class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        
        for idx, val in enumerate(zip(*strs)):
            if(len(set(val))) > 1:
                return strs[0][:idx]
        
        return min(strs)