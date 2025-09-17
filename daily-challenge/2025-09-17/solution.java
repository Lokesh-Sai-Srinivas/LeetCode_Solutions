"""
Problem: 2345 - Design a Food Rating System  
Description: Design a system that supports initializing with lists of foods, their cuisines, and ratings, changing a food's rating, and querying the highest-rated food for a given cuisine (ties broken by lexicographically smaller name).  
Date: 2025-09-17
"""

class FoodRatings {
    private static class Entry {
        String food;
        int rating;
        Entry(String food, int rating) {
            this.food = food;
            this.rating = rating;
        }
    }

    private final Map<String, String> foodToCuisine = new HashMap<>();
    private final Map<String, Integer> foodToRating = new HashMap<>();
    private final Map<String, PriorityQueue<Entry>> cuisineHeaps = new HashMap<>();

    private final Comparator<Entry> cmp = (a, b) -> {
        if (a.rating != b.rating) return Integer.compare(b.rating, a.rating);
        return a.food.compareTo(b.food);
    };

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        for (int i = 0; i < foods.length; ++i) {
            String f = foods[i];
            String c = cuisines[i];
            int r = ratings[i];
            foodToCuisine.put(f, c);
            foodToRating.put(f, r);
            cuisineHeaps.computeIfAbsent(c, k -> new PriorityQueue<>(cmp)).offer(new Entry(f, r));
        }
    }

    public void changeRating(String food, int newRating) {
        String cuisine = foodToCuisine.get(food);
        foodToRating.put(food, newRating);
        cuisineHeaps.get(cuisine).offer(new Entry(food, newRating));
    }

    public String highestRated(String cuisine) {
        PriorityQueue<Entry> heap = cuisineHeaps.get(cuisine);
        while (true) {
            Entry top = heap.peek();
            int current = foodToRating.get(top.food);
            if (top.rating == current) return top.food;
            heap.poll();
        }
    }
}
