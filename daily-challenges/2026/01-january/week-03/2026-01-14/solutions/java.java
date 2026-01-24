import java.util.*;

class Solution {

    static class Event {
        int y, x1, x2, type;
        Event(int y, int x1, int x2, int type) {
            this.y = y;
            this.x1 = x1;
            this.x2 = x2;
            this.type = type;
        }
    }

    static class SegTree {
        int n;
        int[] count;
        long[] len;
        long[] xs;

        SegTree(long[] xs) {
            this.xs = xs;
            this.n = xs.length - 1;
            count = new int[4 * n];
            len = new long[4 * n];
        }

        void update(int node, int l, int r, int ql, int qr, int val) {
            if (qr <= l || r <= ql) return;
            if (ql <= l && r <= qr) {
                count[node] += val;
            } else {
                int mid = (l + r) >> 1;
                update(node << 1, l, mid, ql, qr, val);
                update(node << 1 | 1, mid, r, ql, qr, val);
            }
            if (count[node] > 0) {
                len[node] = xs[r] - xs[l];
            } else if (l + 1 == r) {
                len[node] = 0;
            } else {
                len[node] = len[node << 1] + len[node << 1 | 1];
            }
        }

        long query() {
            return len[1];
        }
    }

    public double separateSquares(int[][] squares) {
        int n = squares.length;
        List<Event> events = new ArrayList<>();
        long[] xs = new long[2 * n];

        for (int i = 0; i < n; i++) {
            int x = squares[i][0], y = squares[i][1], s = squares[i][2];
            events.add(new Event(y, x, x + s, 1));
            events.add(new Event(y + s, x, x + s, -1));
            xs[2 * i] = x;
            xs[2 * i + 1] = x + s;
        }

        Arrays.sort(xs);
        xs = Arrays.stream(xs).distinct().toArray();

        events.sort(Comparator.comparingInt(e -> e.y));

        Map<Long, Integer> xIndex = new HashMap<>();
        for (int i = 0; i < xs.length; i++) {
            xIndex.put(xs[i], i);
        }

        SegTree st = new SegTree(xs);

        double totalArea = 0;
        int prevY = events.get(0).y;

        for (Event e : events) {
            totalArea += st.query() * (e.y - prevY);
            st.update(1, 0, st.n, xIndex.get((long) e.x1), xIndex.get((long) e.x2), e.type);
            prevY = e.y;
        }

        double half = totalArea / 2.0;

        st = new SegTree(xs);
        double area = 0;
        prevY = events.get(0).y;

        for (Event e : events) {
            double next = area + st.query() * (e.y - prevY);
            if (next >= half) {
                return prevY + (half - area) / st.query();
            }
            area = next;
            st.update(1, 0, st.n, xIndex.get((long) e.x1), xIndex.get((long) e.x2), e.type);
            prevY = e.y;
        }

        return prevY;
    }
}