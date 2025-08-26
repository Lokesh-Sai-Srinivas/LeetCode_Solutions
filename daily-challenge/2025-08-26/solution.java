"""
Problem: 3000 - Maximum Area of Longest Diagonal Rectangle  
Description: Given a list of rectangle dimensions, return the area of the rectangle with the longest diagonal. If multiple rectangles share the same diagonal length, return the one with the largest area among them.  
Date: 2025-08-26
"""

class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int max_dia = -1;
        int max_area = 0;
        for (int [] d: dimensions){
            int l = d[0] , w = d[1];
            int dia_sq = l * l + w * w;
            int area = l * w;
            if (dia_sq > max_dia || (dia_sq == max_dia && area > max_area)){
                max_dia = dia_sq;
                max_area = area;
            }
        }
        return max_area;
    }
}
