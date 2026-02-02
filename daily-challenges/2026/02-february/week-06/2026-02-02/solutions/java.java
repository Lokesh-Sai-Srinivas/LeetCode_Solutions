import java.util.*;

class Solution {
    public long minimumCost(int[] nums, int k, int dist) {
        int n = nums.length;
        PriorityQueue<Integer> left = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> right = new PriorityQueue<>();
        Map<Integer, Integer> delayed = new HashMap<>();

        long sum = 0;
        int leftSize = 0;
        long ans = Long.MAX_VALUE;

        for (int i = 1; i <= dist + 1; i++) {
            left.add(nums[i]);
            sum += nums[i];
            leftSize++;
            if (leftSize > k - 1) {
                int x = left.poll();
                sum -= x;
                leftSize--;
                right.add(x);
            }
        }

        ans = sum;

        for (int i = dist + 2; i < n; i++) {
            int out = nums[i - dist - 1];
            delayed.put(out, delayed.getOrDefault(out, 0) + 1);

            if (!left.isEmpty() && out <= left.peek()) {
                sum -= out;
                leftSize--;
            }

            clean(left, delayed);
            clean(right, delayed);

            int in = nums[i];
            if (!left.isEmpty() && in <= left.peek()) {
                left.add(in);
                sum += in;
                leftSize++;
            } else {
                right.add(in);
            }

            if (leftSize < k - 1) {
                clean(right, delayed);
                int x = right.poll();
                left.add(x);
                sum += x;
                leftSize++;
            }

            if (leftSize > k - 1) {
                clean(left, delayed);
                int x = left.poll();
                sum -= x;
                leftSize--;
                right.add(x);
            }

            clean(left, delayed);
            clean(right, delayed);

            ans = Math.min(ans, sum);
        }

        return ans + nums[0];
    }

    private void clean(PriorityQueue<Integer> pq, Map<Integer, Integer> delayed) {
        while (!pq.isEmpty()) {
            int x = pq.peek();
            if (delayed.getOrDefault(x, 0) > 0) {
                pq.poll();
                delayed.put(x, delayed.get(x) - 1);
            } else break;
        }
    }
}