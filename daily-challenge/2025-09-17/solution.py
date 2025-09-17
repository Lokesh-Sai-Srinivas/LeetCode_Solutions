"""
Problem: 2345 - Design a Food Rating System  
Description: Design a system that supports initializing with lists of foods, their cuisines, and ratings, changing a food's rating, and querying the highest-rated food for a given cuisine (ties broken by lexicographically smaller name).  
Date: 2025-09-17
"""

import heapq
from collections import defaultdict
from typing import List

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_heaps = defaultdict(list)  # cuisine -> list of (-rating, food)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            heapq.heappush(self.cuisine_heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        heapq.heappush(self.cuisine_heaps[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            neg_r, name = heap[0]
            if self.food_to_rating.get(name, None) == -neg_r:
                return name
            heapq.heappop(heap)
        return ""  # per problem constraints this line should never be reached
