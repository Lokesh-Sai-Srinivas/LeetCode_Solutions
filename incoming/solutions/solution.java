class Solution {
    public boolean hasAllCodes(String s, int k) {
        Set<String> set = new HashSet<>();
        int n = s.length();

        for(int i = 0; i < n - k + 1; i ++) {
            String temp = s.substring(i, i+k);
            set.add(temp);
        }

        return set.size() == (1<<k);
    }
}
