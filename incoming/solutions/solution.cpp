class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        long long sumAbs = 0L; 
        int negCount = 0;
        int minAbs = 100001;
        bool hasZero = false;

        for(auto &row : matrix){
            for(int val : row){
                if(val == 0) hasZero =  true;
                if(val < 0) negCount ++;
                int ab = abs(val);
                
                sumAbs += ab;
                if(ab < minAbs) minAbs = ab;
            }
        }

        if(negCount % 2 == 0 || hasZero ){
            return sumAbs;
        } 
        return sumAbs - 2L * minAbs;
    }
};
