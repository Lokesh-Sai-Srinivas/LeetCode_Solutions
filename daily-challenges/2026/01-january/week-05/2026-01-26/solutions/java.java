class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        int minVal = Integer.MAX_VALUE, maxVal = Integer.MIN_VALUE;
        for (int num : arr) {
            minVal = Math.min(minVal, num);
            maxVal = Math.max(maxVal, num);
        }

        boolean[] bucket = new boolean[maxVal - minVal + 1];
        for (int num : arr) {
            bucket[num - minVal] = true;
        }

        int prev = -1, minDiff = Integer.MAX_VALUE;
        List<List<Integer>> result = new ArrayList<>();
        
        for (int i = 0; i < bucket.length; i++) {
            if (bucket[i]) {
                if (prev != -1) {
                    int diff = i - prev;
                    if (diff < minDiff) {
                        minDiff = diff;
                        result.clear();
                    }
                    if (diff == minDiff) {
                        result.add(Arrays.asList(prev + minVal, i + minVal));
                    }
                }
                prev = i;
            }
        }
        return result;
    }
}