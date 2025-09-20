"""
Problem: 3508 - Implement Router  
Description: Implement a Router class that supports adding packets with memory limits and no duplicates, forwarding the oldest packet, and counting packets for a destination within a time range.  
Date: 2025-09-20
"""

#include <deque>
#include <unordered_set>
#include <map>
#include <vector>
#include <algorithm>

class Router {
    int memoryLimit;
    std::deque<std::tuple<int, int, int>> queue;
    std::unordered_set<std::string> packetSet;
    std::map<int, std::vector<int>> destMap;

    std::string encode(int s, int d, int t) {
        return std::to_string(s) + "#" + std::to_string(d) + "#" + std::to_string(t);
    }

public:
    Router(int memoryLimit) : memoryLimit(memoryLimit) {}

    bool addPacket(int source, int destination, int timestamp) {
        std::string key = encode(source, destination, timestamp);
        if (packetSet.count(key)) return false;

        if (queue.size() == memoryLimit) {
            auto [s, d, t] = queue.front();
            queue.pop_front();
            packetSet.erase(encode(s, d, t));
            auto& vec = destMap[d];
            vec.erase(std::lower_bound(vec.begin(), vec.end(), t));
        }

        queue.emplace_back(source, destination, timestamp);
        packetSet.insert(key);
        auto& vec = destMap[destination];
        vec.insert(std::upper_bound(vec.begin(), vec.end(), timestamp), timestamp);
        return true;
    }

    std::vector<int> forwardPacket() {
        if (queue.empty()) return {};
        auto [s, d, t] = queue.front();
        queue.pop_front();
        packetSet.erase(encode(s, d, t));
        auto& vec = destMap[d];
        vec.erase(std::lower_bound(vec.begin(), vec.end(), t));
        return {s, d, t};
    }

    int getCount(int destination, int startTime, int endTime) {
        auto& vec = destMap[destination];
        auto left = std::lower_bound(vec.begin(), vec.end(), startTime);
        auto right = std::upper_bound(vec.begin(), vec.end(), endTime);
        return right - left;
    }
};
