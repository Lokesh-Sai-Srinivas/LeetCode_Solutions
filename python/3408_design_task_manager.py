"""
Problem: 3408 - Design Task Manager  
Description: Design a TaskManager class that supports initializing with a list of tasks (each with userId, taskId, and priority), adding new tasks, editing task priorities, removing tasks, and executing the highest-priority task. If multiple tasks share the same priority, execute the one with the smallest taskId. Return the userId of the executed task, or -1 if no valid task exists.  
Date: 2025-09-18  
"""

import heapq

class TaskManager:
    def __init__(self, tasks):
        self.task_map = {}  # taskId → (userId, priority)
        self.heap = []      # max heap: (-priority, -taskId, taskId)

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self):
        while self.heap:
            neg_priority, neg_taskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                userId, current_priority = self.task_map[taskId]
                if -neg_priority == current_priority:
                    del self.task_map[taskId]
                    return userId
        return -1

