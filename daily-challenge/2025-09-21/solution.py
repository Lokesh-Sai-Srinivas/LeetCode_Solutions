"""
Problem: 1912 - Design Movie Rental System  
Description: Implement a MovieRentingSystem class that supports searching for available movies by price, renting and dropping movies, and reporting the top 5 rented movies sorted by price and shop ID.  
Date: 2025-09-21
"""

from sortedcontainers import SortedList

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.available = {}  # movie -> SortedList of (price, shop)
        self.rented = SortedList()  # (price, shop, movie)
        self.priceMap = {}

        for shop, movie, price in entries:
            if movie not in self.available:
                self.available[movie] = SortedList()
            self.available[movie].add((price, shop))
            self.priceMap[(shop, movie)] = price

    def search(self, movie: int) -> list[int]:
        if movie not in self.available:
            return []
        return [shop for price, shop in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.priceMap[(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.priceMap[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        return [[shop, movie] for price, shop, movie in self.rented[:5]]
