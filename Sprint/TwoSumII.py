class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l < r:
            temp = target - numbers[l]
            if numbers[r] == temp:
                return [l + 1, r + 1]
            elif numbers[r] > temp:
                r -= 1
            else:
                l += 1
        
        return []