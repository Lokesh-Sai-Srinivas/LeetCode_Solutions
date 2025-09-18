"""
Problem: 3408 - Design Task Manager  
Description: Design a TaskManager class that supports initializing with a list of tasks (each with userId, taskId, and priority), adding new tasks, editing task priorities, removing tasks, and executing the highest-priority task. If multiple tasks share the same priority, execute the one with the smallest taskId. Return the userId of the executed task, or -1 if no valid task exists.  
Date: 2025-09-18  
"""

import java.util.*;

class TaskManager {
    private Map<Integer, int[]> taskMap; // taskId → [userId, priority]
    private PriorityQueue<int[]> maxHeap; // [priority, taskId]

    public TaskManager(List<List<Integer>> tasks) {
        taskMap = new HashMap<>();
        maxHeap = new PriorityQueue<>((a, b) -> {
            if (b[0] != a[0]) return b[0] - a[0]; // higher priority first
            return b[1] - a[1]; // tie-breaker: higher taskId first
        });

        for (List<Integer> t : tasks) {
            add(t.get(0), t.get(1), t.get(2));
        }
    }

    public void add(int userId, int taskId, int priority) {
        taskMap.put(taskId, new int[]{userId, priority});
        maxHeap.offer(new int[]{priority, taskId});
    }

    public void edit(int taskId, int newPriority) {
        int userId = taskMap.get(taskId)[0];
        taskMap.put(taskId, new int[]{userId, newPriority});
        maxHeap.offer(new int[]{newPriority, taskId});
    }

    public void rmv(int taskId) {
        taskMap.remove(taskId);
    }

    public int execTop() {
        while (!maxHeap.isEmpty()) {
            int[] top = maxHeap.poll();
            int priority = top[0], taskId = top[1];
            if (taskMap.containsKey(taskId) && taskMap.get(taskId)[1] == priority) {
                int userId = taskMap.get(taskId)[0];
                taskMap.remove(taskId);
                return userId;
            }
        }
        return -1;
    }
}
