"""
Problem: 1733 - Minimum Number of People to Teach  
Description: You are given an integer n representing the number of languages, a 2D array languages where languages[i] is the list of languages the i-th person knows, and a 2D array friendships where friendships[j] = [u, v] denotes a friendship between person u and person v. Two people can communicate if they share at least one common language. You may choose one language and teach it to some people so that all friends can communicate with each other. Return the minimum number of people you need to teach.  
Date: 2025-09-10  
"""

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
