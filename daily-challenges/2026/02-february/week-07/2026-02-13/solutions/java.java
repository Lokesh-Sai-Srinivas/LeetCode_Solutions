import java.util.*;

class Solution {
    public int longestBalanced(String s) {
        int n = s.length();
        if (n == 0) return 0;

        int ans = 0;

        int run = 1;
        for (int i = 1; i < n; i++) {
            if (s.charAt(i) == s.charAt(i - 1)) run++;
            else {
                ans = Math.max(ans, run);
                run = 1;
            }
        }
        ans = Math.max(ans, run);

        int a = 0, b = 0, c = 0;
        HashMap<Long, Integer> map = new HashMap<>();
        map.put(0L, -1);
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);
            if (ch == 'a') a++;
            else if (ch == 'b') b++;
            else c++;
            int x = a - b;
            int y = a - c;
            long key = (((long) x) << 32) ^ (y & 0xffffffffL);
            if (map.containsKey(key)) {
                ans = Math.max(ans, i - map.get(key));
            } else {
                map.put(key, i);
            }
        }

        char[] arr = {'a', 'b', 'c'};
        for (char z : arr) {
            int i = 0;
            while (i < n) {
                while (i < n && s.charAt(i) == z) i++;
                if (i >= n) break;
                int l = i;
                while (i < n && s.charAt(i) != z) i++;
                int r = i - 1;

                char x = 0, y = 0;
                for (char t : arr) {
                    if (t != z) {
                        if (x == 0) x = t;
                        else y = t;
                    }
                }

                HashMap<Integer, Integer> dif = new HashMap<>();
                dif.put(0, l - 1);
                int d = 0;
                for (int j = l; j <= r; j++) {
                    char ch = s.charAt(j);
                    if (ch == x) d++;
                    else if (ch == y) d--;
                    if (dif.containsKey(d)) {
                        ans = Math.max(ans, j - dif.get(d));
                    } else {
                        dif.put(d, j);
                    }
                }
            }
        }

        return ans;
    }
}