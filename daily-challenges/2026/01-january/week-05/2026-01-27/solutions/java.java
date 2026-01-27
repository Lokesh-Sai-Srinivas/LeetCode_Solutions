class Solution {
    public int minCost(int n, int[][] edges) {
        Map<Integer, List<int[]> > map = new HashMap<>();
        for(int [] ele : edges){
            int ui = ele[0];
            int vi = ele[1];
            int wi = ele[2];

            map.computeIfAbsent(ui, k -> new ArrayList<>()).add(new int[]{vi,wi});
            map.computeIfAbsent(vi, k -> new ArrayList<>()).add(new int[]{ui,2 * wi});
        }

        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;

        PriorityQueue<int []> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.offer(new int[]{0,0});
        

        while(!pq.isEmpty()) {
            int[] cur = pq.poll();
            int u = cur[0], cost = cur[1];

            if(u == n - 1) return cost;
            if(cost > dist[u]) continue;

            for(int[] ele: map.getOrDefault(u, Collections.emptyList())) {
                int v = ele[0], w = ele[1];
                if(dist[v] > cost + w) {
                    dist[v] = cost + w;
                    pq.offer(new int[] {v, dist[v]});
                }
            }
        }

        return -1;
    }
}