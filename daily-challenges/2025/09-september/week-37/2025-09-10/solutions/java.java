class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        List<Set<Integer>> langSets = new ArrayList<>();
        for (int[] l : languages) {
            Set<Integer> set = new HashSet<>();
            for (int lang : l) set.add(lang);
            langSets.add(set);
        }

        Set<Integer> needTeachUsers = new HashSet<>();
        for (int[] f : friendships) {
            int u = f[0] - 1, v = f[1] - 1;
            Set<Integer> setU = langSets.get(u);
            Set<Integer> setV = langSets.get(v);
            boolean canCommunicate = false;
            for (int lang : setU) {
                if (setV.contains(lang)) {
                    canCommunicate = true;
                    break;
                }
            }
            if (!canCommunicate) {
                needTeachUsers.add(u);
                needTeachUsers.add(v);
            }
        }

        int minTeach = Integer.MAX_VALUE;
        for (int lang = 1; lang <= n; lang++) {
            int count = 0;
            for (int user : needTeachUsers) {
                if (!langSets.get(user).contains(lang)) {
                    count++;
                }
            }
            minTeach = Math.min(minTeach, count);
        }

        return minTeach;
    }
}