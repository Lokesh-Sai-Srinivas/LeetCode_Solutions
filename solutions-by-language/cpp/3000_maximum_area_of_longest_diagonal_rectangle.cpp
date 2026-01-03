class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        int max_dia = -1;
        int max_area = 0;

        for (auto& d : dimensions) {
            int l = d[0], w = d[1];
            int dia_sq = l * l + w * w;
            int area = l * w;
            if (dia_sq > max_dia || (dia_sq == max_dia && area > max_area)){
                max_dia = dia_sq;
                max_area = area;
            }
        }
        return max_area;
    }
};