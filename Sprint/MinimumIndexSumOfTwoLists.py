class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        restaurants = {}
        final_restaurants = {}
        
        for idx, restaurant in enumerate(list1):
            restaurants[restaurant] = idx
        
        for idx, restaurant in enumerate(list2):
            if restaurant in restaurants:
                final_restaurants[restaurant] = idx
                final_restaurants[restaurant] += restaurants[restaurant]
        
        min_index = min(value for value in final_restaurants.values())
        return [restaurant for restaurant, index in final_restaurants.items() if index == min_index]
