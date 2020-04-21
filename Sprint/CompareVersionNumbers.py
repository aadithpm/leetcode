class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i, j = 0, 0
        while i < len(version1) and j < len(version2):
            prev_i = i
            while i < len(version1) and version1[i] != '.':
                i += 1
            str1 = str(version1[prev_i : i])

            prev_j = j
            while j < len(version2) and version2[j] != '.':
                j += 1
            str2 = str(version2[prev_j : j])

            if(int(str1) > int(str2)):
                return 1

            elif(int(str1) < int(str2)):
                return -1
            
            i += 1
            j += 1

        while i < len(version1):
            if(version1[i] != '.' and version1[i] != '0'):
                return 1
            i += 1

        while j < len(version2):
            if(version2[j] != '.' and version2[j] != '0'):
                return -1
            j += 1

        return 0
