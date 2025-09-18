"""
Problem: 3408 - Design Task Manager  
Description: Design a TaskManager class that supports initializing with a list of tasks (each with userId, taskId, and priority), adding new tasks, editing task priorities, removing tasks, and executing the highest-priority task. If multiple tasks share the same priority, execute the one with the smallest taskId. Return the userId of the executed task, or -1 if no valid task exists.  
Date: 2025-09-18  
"""

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
