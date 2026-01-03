using namespace std;

class Solution {
public:
    long long minOperations(vector<vector<int>>& queries) {
        long long total = 0;
        for (auto &q : queries) {
            total += opsForRange(q[0], q[1]);
        }
        return total;
    }

private:
    long long opsForRange(long long l, long long r) {
        long long stepsSum = 0;
        long long start = 1;
        int level = 1;

        while (start <= r) {
            long long end = start * 4 - 1;
            long long left = max(l, start);
            long long right = min(r, end);

            if (left <= right) {
                long long count = right - left + 1;
                stepsSum += count * level;
            }

            start *= 4;
            level++;
        }

        return (stepsSum + 1) / 2; 
    }
};