class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        # ["/a","/c/d","/c/f"]
        directories = {}
        folders = sorted(folder, key = len)
        for folder in folders:
            found = False
            for directory, slashes in directories.items():
                if directory in folder and folder.count('/') > slashes:
                    found = True
                    break
            
            if not found:
                directories[folder] = folder.count('/')
            
        return sorted(list(directories.keys()))
