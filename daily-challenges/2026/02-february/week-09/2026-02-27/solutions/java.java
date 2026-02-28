class Solution {
    public int minOperations(String s, int k) {
        int n = s.length();

        int count0 = 0;

        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '0')
                count0++;
        }

        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        dist[count0] = 0;

        TreeSet<Integer>[] unvisited = new TreeSet[2];
        unvisited[0] = new TreeSet<>();
        unvisited[1] = new TreeSet<>();

        for (int i = 0; i <= n; i++) {
            if (i != count0)
                unvisited[i % 2].add(i);
        }

        Deque<Integer> q = new ArrayDeque<>();
        q.add(count0);

        while (!q.isEmpty()) {
            int c = q.poll();

            int xMin = Math.max(0, k - (n - c));
            int xMax = Math.min(k, c);
            if (xMin > xMax)
                continue;

            int cLow = c + k - 2 * xMax;
            int cHigh = c + k - 2 * xMin;
            int parity = (c + k) & 1;

            TreeSet<Integer> set = unvisited[parity];
            if (set.isEmpty())
                continue; 
            Integer from = set.ceiling(cLow); 
            if (from == null || from > cHigh) continue;
            List<Integer> toVisit = new ArrayList<>(); 
            Iterator<Integer> it = set.tailSet(cLow, true).iterator(); 
            while (it.hasNext()) { 
                int val = it.next(); 
                if (val > cHigh) break; 
                toVisit.add(val); 
            } 
            for (int val : toVisit) { 
                set.remove(val); 
                dist[val] = dist[c] + 1; 
                if (val == 0) return dist[val]; 
                q.add(val); 
            } 
        } 
        return dist[0];
    }
}