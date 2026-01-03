#include <unordered_map>
#include <queue>
#include <vector>
using namespace std;

class TaskManager {
    unordered_map<int, pair<int, int>> taskMap; // taskId → {userId, priority}
    priority_queue<tuple<int, int, int>> maxHeap; // {priority, taskId, taskId}

public:
    TaskManager(vector<vector<int>>& tasks) {
        for (auto& t : tasks) {
            add(t[0], t[1], t[2]);
        }
    }

    void add(int userId, int taskId, int priority) {
        taskMap[taskId] = {userId, priority};
        maxHeap.emplace(priority, taskId, taskId);
    }

    void edit(int taskId, int newPriority) {
        int userId = taskMap[taskId].first;
        taskMap[taskId] = {userId, newPriority};
        maxHeap.emplace(newPriority, taskId, taskId);
    }

    void rmv(int taskId) {
        taskMap.erase(taskId);
    }

    int execTop() {
        while (!maxHeap.empty()) {
            auto [priority, taskId, _] = maxHeap.top();
            maxHeap.pop();
            if (taskMap.count(taskId) && taskMap[taskId].second == priority) {
                int userId = taskMap[taskId].first;
                taskMap.erase(taskId);
                return userId;
            }
        }
        return -1;
    }
};