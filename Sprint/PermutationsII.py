class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = [[]]
        for num in nums:
            temp = []
            for item in ret:
                print(item)
                for i in range(len(item) + 1):
                    temp.append(item[:i] + [num] + item[i:])
                    if i < len(item) and item[i] == num:
                        break
            ret = temp
        return ret if any(ret) else []
    
