class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def csort(log):
            _id, content = log.split(" ", 1)
            return (0, content, _id) if content[0].isalpha() else (1,)
        
        return sorted(logs, key = csort)
