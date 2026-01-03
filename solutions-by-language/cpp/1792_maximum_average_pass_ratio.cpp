class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        auto gain = [](int p, int t) {
            return (double)(p + 1) / (t + 1) - (double)p / t;
        };

        priority_queue<pair<double, pair<int, int>>> pq;

        for (auto& cls : classes) {
            pq.push({gain(cls[0], cls[1]), {cls[0], cls[1]}});
        }

        while (extraStudents--) {
            auto [g, pt] = pq.top(); pq.pop();
            int p = pt.first + 1;
            int t = pt.second + 1;
            pq.push({gain(p, t), {p, t}});
        }

        double total = 0.0;
        while (!pq.empty()) {
            auto [_, pt] = pq.top(); pq.pop();
            total += (double)pt.first / pt.second;
        }

        return total / classes.size();
    }
};