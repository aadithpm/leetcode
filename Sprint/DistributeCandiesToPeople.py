class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        people_candies = [0] * num_people
        max_so_far = 0
        while candies > 0:
            for i in range(num_people):
                if candies < 1:
                    break
                added_candies = min(1 + max_so_far, candies)
                people_candies[i] += added_candies
                max_so_far = added_candies
                candies -= max_so_far
        return people_candies
