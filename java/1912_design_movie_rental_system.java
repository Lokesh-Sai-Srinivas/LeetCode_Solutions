"""
Problem: 1912 - Design Movie Rental System  
Description: Implement a MovieRentingSystem class that supports searching for available movies by price, renting and dropping movies, and reporting the top 5 rented movies sorted by price and shop ID.  
Date: 2025-09-21
"""

import java.util.*;

class MovieRentingSystem {
    private Map<Integer, TreeSet<int[]>> available; // movie -> {(price, shop)}
    private TreeSet<int[]> rented; // {(price, shop, movie)}
    private Map<String, Integer> priceMap; // "shop#movie" -> price

    public MovieRentingSystem(int n, int[][] entries) {
        available = new HashMap<>();
        rented = new TreeSet<>((a, b) -> 
            a[0] != b[0] ? a[0] - b[0] : 
            a[1] != b[1] ? a[1] - b[1] : 
            a[2] - b[2]);
        priceMap = new HashMap<>();

        for (int[] e : entries) {
            int shop = e[0], movie = e[1], price = e[2];
            available.computeIfAbsent(movie, k -> new TreeSet<>((x, y) -> 
                x[0] != y[0] ? x[0] - y[0] : x[1] - y[1]))
                .add(new int[]{price, shop});
            priceMap.put(shop + "#" + movie, price);
        }
    }

    public List<Integer> search(int movie) {
        List<Integer> res = new ArrayList<>();
        if (!available.containsKey(movie)) return res;
        for (int[] e : available.get(movie)) {
            if (res.size() == 5) break;
            res.add(e[1]);
        }
        return res;
    }

    public void rent(int shop, int movie) {
        int price = priceMap.get(shop + "#" + movie);
        available.get(movie).remove(new int[]{price, shop});
        rented.add(new int[]{price, shop, movie});
    }

    public void drop(int shop, int movie) {
        int price = priceMap.get(shop + "#" + movie);
        rented.remove(new int[]{price, shop, movie});
        available.get(movie).add(new int[]{price, shop});
    }

    public List<List<Integer>> report() {
        List<List<Integer>> res = new ArrayList<>();
        for (int[] e : rented) {
            if (res.size() == 5) break;
            res.add(Arrays.asList(e[1], e[2]));
        }
        return res;
    }
}
