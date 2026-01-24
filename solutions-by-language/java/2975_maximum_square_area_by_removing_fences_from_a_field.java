class Solution {
    private static final long mod = 1_000_000_007L;
    public int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {
        Arrays.sort(hFences);
        Arrays.sort(vFences);

        List<Integer> h = new ArrayList<>();
        List<Integer> v = new ArrayList<>();

        h.add(1);
        for (int x : hFences) h.add(x);
        h.add(m);

        v.add(1);
        for (int x : vFences) v.add(x);
        v.add(n);

        Set<Long> vDiffs = new HashSet<>();
        for (int i = 0; i < v.size(); i++) {
            for (int j = i + 1; j < v.size(); j++) {
                vDiffs.add((long) v.get(j) - v.get(i));
            }
        }

        long maxSide = -1;
        for (int i = 0; i < h.size(); i++) {
            for (int j = i + 1; j < h.size(); j++) {
                long d = (long) h.get(j) - h.get(i);
                if (vDiffs.contains(d)) {
                    maxSide = Math.max(maxSide, d);
                }
            }
        }

        if (maxSide == -1) return -1;
        return (int) ((maxSide % mod) * (maxSide % mod) % mod);
    }
}