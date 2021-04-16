package fbhackercup.s2016.round1.b;

import java.io.*;
import java.util.Arrays;
import java.util.Comparator;

class B {
    private static void main(PrintWriter out) throws IOException {
        long l = Parser.nextLong();
        long n = Parser.nextLong();
        long m = Parser.nextLong();
        long d = Parser.nextLong();
        long[] w = new long[(int) n];
        for (int i = 0; i < n; i++) {
            w[i] = Parser.nextInt();
        }

        Heap wmHeap = new Heap(n, w);
        long dryers = Math.min(l, m);
        long[] cost = new long[(int) dryers];
        Arrays.fill(cost, d);
        Heap dHeap = new Heap(dryers, cost);

        for (int i = 0; i < l; i++) {
            long nextEnd = wmHeap.incRoot();
            dHeap.incRoot(nextEnd);
        }
        out.println(dHeap.max());
    }

    static class Pair {
        long a;
        long b;

        public Pair(long a, long b) {
            this.a = a;
            this.b = b;
        }

        @Override
        public String toString() {
            return String.valueOf(a) + ":" + String.valueOf(b);
        }
    }

    static class Heap {
        Pair[] heap;
        private final long n;

        public Heap(long n, long[] w) {
            this.n = n;
            heap = new Pair[(int) n + 1];
            heap[0] = new Pair(-1, -1);
            for (int i = 0; i < n; i++) {
                heap[i + 1] = new Pair(w[i], w[i]);
            }
            Arrays.sort(heap, new Comparator<Pair>() {
                @Override
                public int compare(Pair o1, Pair o2) {
                    return Long.compare(o1.a, o2.a);
                }
            });
        }

        public long incRoot() {
            long res = heap[1].a;
            heap[1].a += heap[1].b;
            int cur = 1;
            while (true) {
                int l = cur * 2;
                int r = l + 1;
                int next = cur;
                if (l <= n && heap[cur].a > heap[l].a) {
                    next = l;
                }
                if (r <= n && heap[next].a > heap[r].a) {
                    next = r;
                }
                if (next == cur) {
                    break;
                } else {
                    swap(cur, next);
                    cur = next;
                }
            }
            return res;
        }

        private void swap(int i1, int i2) {
            Pair pom = heap[i1];
            heap[i1] = heap[i2];
            heap[i2] = pom;
        }

        public long max() {
            long res = Long.MIN_VALUE;
            for (int i = 0; i < n + 1; i++) {
                res = Math.max(res, heap[i].a - heap[i].b);
            }
            return res;
        }

        public void incRoot(long m) {
            heap[1].a = Math.max(m, heap[1].a - heap[1].b) + heap[1].b;
            incRoot();
        }
    }

    // Prewritten code

    public static void main(String[] args) throws IOException {
        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            out.print("Case #" + (tt + 1) + ": ");
            main(out);
        }
        out.close();
    }

    private static class Parser {
        private static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        private static String line;
        private static int indexAfterLastToken = 0;

        private static Integer nextInt() throws IOException {
            return Integer.parseInt(nextToken());
        }

        private static Long nextLong() throws IOException {
            return Long.parseLong(nextToken());
        }

        private static String nextString() throws IOException {
            return nextToken();
        }

        private static Double nextDouble() throws IOException {
            return Double.parseDouble(nextToken());
        }

        private static String nextLine() throws IOException {
            return in.readLine();
        }

        private static String nextToken() throws IOException {
            if (line == null) line = in.readLine();
            if (line == null) {
                throw new IOException();
            } else {
                line = line.trim();

                int indexAfterNextToken = line.indexOf(" ", indexAfterLastToken);
                while (indexAfterNextToken == indexAfterLastToken) { // skip spaces
                    indexAfterLastToken += 1;
                    indexAfterNextToken = line.indexOf(" ", indexAfterLastToken);
                }

                String res;
                if (indexAfterNextToken == -1) {
                    res = line.substring(indexAfterLastToken);
                    line = null;
                    indexAfterLastToken = 0;
                } else {
                    res = line.substring(indexAfterLastToken, indexAfterNextToken);
                    indexAfterLastToken = indexAfterNextToken + 1;
                }
                return res;
            }
        }
    }
}
