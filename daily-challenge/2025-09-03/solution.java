"""
Problem: 3027 - Find the Number of Ways to Place People II  
Description: You are given a list of 2D coordinates representing people on a grid. Count the number of valid pairs (i, j) such that person i is to the left of person j, person i’s y-coordinate is greater than or equal to person j’s y-coordinate, and there is no other person between them blocking the view.  
Date: 2025-09-03
"""
class Solution {
    public int numberOfPairs(int[][] points) {
        // Sort by x ascending, then y descending
        Arrays.sort(points, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]);
        });

        int n = points.length;
        int ans = 0;

        for (int j = 0; j < n; j++) { // Bob at j
            int yj = points[j][1];
            int m = Integer.MAX_VALUE; // min y among blocking points

            for (int i = j - 1; i >= 0; i--) { // Alice to the left
                // Include the immediate right neighbor into the "between" set
                if (i + 1 < j) {
                    int yr = points[i + 1][1];
                    if (yr >= yj && yr < m) {
                        m = yr;
                    }
                }
                int yi = points[i][1];
                // Valid if yi >= yj and no blocking point in (i, j)
                if (yi >= yj && yi < m) {
                    ans++;
                }
            }
        }
        return ans;
    }
}
