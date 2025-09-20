"""
Problem: 3508 - Implement Router  
Description: Implement a Router class that supports adding packets with memory limits and no duplicates, forwarding the oldest packet, and counting packets for a destination within a time range.  
Date: 2025-09-20
"""

from collections import deque, defaultdict
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # FIFO queue of packets
        self.packetSet = set()  # To detect duplicates
        self.destMap = defaultdict(list)  # destination -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packetSet:
            return False

        if len(self.queue) == self.memoryLimit:
            old = self.queue.popleft()
            self.packetSet.remove(old)
            self.destMap[old[1]].remove(old[2])  # remove timestamp from destination map

        self.queue.append(key)
        self.packetSet.add(key)
        bisect.insort(self.destMap[destination], timestamp)
        return True

    def forwardPacket(self) -> list[int]:
        if not self.queue:
            return []
        packet = self.queue.popleft()
        self.packetSet.remove(packet)
        self.destMap[packet[1]].remove(packet[2])
        return list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destMap[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left
