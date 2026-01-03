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