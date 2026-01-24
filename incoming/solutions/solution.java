class Solution {
    public int minimumPairRemoval(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;

        long[] val = new long[n];
        for (int i = 0; i < n; i++) val[i] = nums[i];

        int[] left = new int[n];
        int[] right = new int[n];
        boolean[] alive = new boolean[n];

        for (int i = 0; i < n; i++) {
            left[i] = i - 1;
            right[i] = i + 1;
            alive[i] = true;
        }

        PriorityQueue<long[]> pq = new PriorityQueue<>(
            (a, b) -> a[0] != b[0] ? Long.compare(a[0], b[0]) : Long.compare(a[1], b[1])
        );

        int bad = 0;
        for (int i = 0; i + 1 < n; i++) {
            if (val[i] > val[i + 1]) bad++;
            pq.add(new long[]{val[i] + val[i + 1], i});
        }

        int ops = 0;

        while (bad > 0 && !pq.isEmpty()) {
            long[] cur = pq.poll();
            int i = (int) cur[1];
            int j = right[i];

            if (j >= n || !alive[i] || !alive[j]) continue;
            if (val[i] + val[j] != cur[0]) continue;

            int li = left[i];
            int rj = right[j];

            if (li != -1 && val[li] > val[i]) bad--;
            if (val[i] > val[j]) bad--;
            if (rj < n && val[j] > val[rj]) bad--;

            val[i] += val[j];
            alive[j] = false;
            right[i] = rj;
            if (rj < n) left[rj] = i;

            if (li != -1 && val[li] > val[i]) bad++;
            if (rj < n && val[i] > val[rj]) bad++;

            if (li != -1) pq.add(new long[]{val[li] + val[i], li});
            if (rj < n) pq.add(new long[]{val[i] + val[rj], i});

            ops++;
        }

        return ops;
    }
}
