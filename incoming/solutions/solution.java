class Solution {
    private static final Map<Integer, List<String>> map = new HashMap<>();

    static {
        for(int h = 0; h < 12; h ++) {
            for (int m = 0; m < 60; m ++) {
                int bits = Integer.bitCount(h) + Integer.bitCount(m);
                map.computeIfAbsent(bits, k -> new ArrayList<>()) .add(String.format("%d:%02d", h, m));
            }
        }
    }
    public List<String> readBinaryWatch(int turnedOn) {
        return map.getOrDefault(turnedOn, Collections.emptyList());
    }
}
