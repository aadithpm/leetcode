class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nums_copy = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.nums_copy
        self.nums_copy = list(self.nums_copy)
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        temp_array = list(self.nums)
        for i in range(len(self.nums)):
            idx = random.randrange(len(temp_array))
            self.nums[i], self.nums[idx] = self.nums[idx], self.nums[i]

        return self.nums