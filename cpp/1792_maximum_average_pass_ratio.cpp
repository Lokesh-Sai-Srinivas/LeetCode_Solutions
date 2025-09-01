"""
Problem: 1792 - Maximum Average Pass Ratio  
Description: You are given a list of classes, each represented by [pass_i, total_i], and an integer extraStudents. Each extra student is guaranteed to pass any class they are assigned to. Assign these students to classes to maximize the average pass ratio across all classes. The pass ratio of a class is pass_i / total_i. Return the maximum possible average pass ratio after assigning all extra students.  
Date: 2025-09-01
"""

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
