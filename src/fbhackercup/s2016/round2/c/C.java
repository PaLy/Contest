package fbhackercup.s2016.round2.c;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;

class C {
    private static void main(PrintWriter out) throws IOException {
        int n = Parser.nextInt();
        Ladder[] ladders = new Ladder[n];
        for (int i = 0; i < n; i++) {
            ladders[i] = new Ladder(Parser.nextLong(), Parser.nextLong());
        }
        Arrays.sort(ladders, new Comparator<Ladder>() {
            @Override
            public int compare(Ladder o1, Ladder o2) {
                return Long.compare(o1.x, o2.x);
            }
        });
        long MOD = 1000000000 + 7;
        long res = 0;
        System.out.println(Arrays.toString(ladders));
        ArrayList<Ladder> s = new ArrayList<>();
        s.add(ladders[0]);
        for (int i = 1; i < n; i++) {
            long curx = ladders[i].x;
            long curh = ladders[i].h;
            Collections.sort(s, new Comparator<Ladder>() {
                @Override
                public int compare(Ladder o1, Ladder o2) {
                    return -Long.compare(o1.h, o2.h);
                }
            });
            while (s.size() > 0 && s.get(s.size() - 1).h < curh) {
                s.remove(s.size() - 1);
            }
            int k = s.size() - 1;
            while (k >= 0 && s.get(k).h == curh) {
                res += (curx - s.get(k).x) * (curx - s.get(k).x);
                res %= MOD;
                k--;
            }
            s.add(ladders[i]);
        }
        out.println(res);
    }

    static class Ladder {
        long x;

        public Ladder(long x, long h) {
            this.x = x;
            this.h = h;
        }

        @Override
        public String toString() {
            return "x=" + x +
                    ", h=" + h
                    ;
        }

        long h;
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
