class Solution {
    static class Node {
        int l, r, mn, mx, lazy;
    }

    static class SegTree {
        Node[] t;

        SegTree(int n) {
            t = new Node[n << 2];
            for (int i = 0; i < t.length; i++) t[i] = new Node();
            build(1, 0, n);
        }

        void build(int u, int l, int r) {
            t[u].l = l; t[u].r = r;
            t[u].mn = t[u].mx = 0;
            t[u].lazy = 0;
            if (l == r) return;
            int m = (l + r) >> 1;
            build(u << 1, l, m);
            build(u << 1 | 1, m + 1, r);
        }

        void add(int u, int l, int r, int v) {
            if (t[u].l >= l && t[u].r <= r) {
                apply(u, v);
                return;
            }
            push(u);
            int m = (t[u].l + t[u].r) >> 1;
            if (l <= m) add(u << 1, l, r, v);
            if (r > m) add(u << 1 | 1, l, r, v);
            up(u);
        }

        int find(int u, int val) {
            if (t[u].l == t[u].r) return t[u].l;
            push(u);
            int L = u << 1, R = u << 1 | 1;
            if (t[L].mn <= val && val <= t[L].mx) return find(L, val);
            return find(R, val);
        }

        void apply(int u, int v) {
            t[u].mn += v; t[u].mx += v; t[u].lazy += v;
        }

        void up(int u) {
            t[u].mn = Math.min(t[u << 1].mn, t[u << 1 | 1].mn);
            t[u].mx = Math.max(t[u << 1].mx, t[u << 1 | 1].mx);
        }

        void push(int u) {
            if (t[u].lazy != 0) {
                apply(u << 1, t[u].lazy);
                apply(u << 1 | 1, t[u].lazy);
                t[u].lazy = 0;
            }
        }
    }

    public int longestBalanced(int[] a) {
        int n = a.length;
        SegTree st = new SegTree(n);
        Map<Integer, Integer> last = new HashMap<>();
        int cur = 0, res = 0;

        for (int i = 1; i <= n; i++) {
            int x = a[i - 1];
            int d = (x & 1) == 1 ? 1 : -1;
            if (last.containsKey(x)) {
                st.add(1, last.get(x), n, -d);
                cur -= d;
            }
            last.put(x, i);
            st.add(1, i, n, d);
            cur += d;
            int pos = st.find(1, cur);
            res = Math.max(res, i - pos);
        }
        return res;
    }
}