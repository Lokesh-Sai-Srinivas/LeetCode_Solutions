"""
Problem: 3508 - Implement Router  
Description: Implement a Router class that supports adding packets with memory limits and no duplicates, forwarding the oldest packet, and counting packets for a destination within a time range.  
Date: 2025-09-20
"""

import java.util.*;

class Router {
    private int memoryLimit;
    private Deque<int[]> queue;
    private Set<String> packetSet;
    private Map<Integer, List<Integer>> destMap;

    public Router(int memoryLimit) {
        this.memoryLimit = memoryLimit;
        this.queue = new LinkedList<>();
        this.packetSet = new HashSet<>();
        this.destMap = new HashMap<>();
    }

    // Encode a packet as "source#destination#timestamp"
    private String encode(int s, int d, int t) {
        return s + "#" + d + "#" + t;
    }

    // Add a packet if not duplicate; evict oldest if at capacity
    public boolean addPacket(int source, int destination, int timestamp) {
        String key = encode(source, destination, timestamp);
        if (packetSet.contains(key)) {
            return false;
        }

        // Evict oldest packet when memoryLimit reached
        if (queue.size() == memoryLimit) {
            int[] old = queue.pollFirst();
            packetSet.remove(encode(old[0], old[1], old[2]));
            List<Integer> oldList = destMap.get(old[1]);
            int oldIdx = Collections.binarySearch(oldList, old[2]);
            if (oldIdx >= 0) oldList.remove(oldIdx);
        }

        // Enqueue new packet
        queue.offerLast(new int[] { source, destination, timestamp });
        packetSet.add(key);

        // Insert timestamp into sorted list for that destination
        destMap.computeIfAbsent(destination, k -> new ArrayList<>());
        List<Integer> list = destMap.get(destination);
        int idx = Collections.binarySearch(list, timestamp);
        if (idx < 0) idx = -idx - 1;
        list.add(idx, timestamp);

        return true;
    }

    // Forward (dequeue) the oldest packet
    public int[] forwardPacket() {
        if (queue.isEmpty()) {
            return new int[0];
        }
        int[] pkt = queue.pollFirst();
        packetSet.remove(encode(pkt[0], pkt[1], pkt[2]));

        List<Integer> list = destMap.get(pkt[1]);
        int idx = Collections.binarySearch(list, pkt[2]);
        if (idx >= 0) list.remove(idx);

        return pkt;
    }

    // Count packets for a given destination within [startTime, endTime]
    public int getCount(int destination, int startTime, int endTime) {
        List<Integer> list = destMap.getOrDefault(destination, new ArrayList<>());

        // Find first index ≥ startTime
        int leftIndex = Collections.binarySearch(list, startTime);
        int left;
        if (leftIndex < 0) {
            left = -leftIndex - 1;
        } else {
            left = leftIndex;
            while (left > 0 && list.get(left - 1) == startTime) {
                left--;
            }
        }

        // Find first index > endTime
        int rightIndex = Collections.binarySearch(list, endTime);
        int right;
        if (rightIndex < 0) {
            right = -rightIndex - 1;
        } else {
            right = rightIndex;
            while (right + 1 < list.size() && list.get(right + 1) == endTime) {
                right++;
            }
            right++;
        }

        return right - left;
    }
}
