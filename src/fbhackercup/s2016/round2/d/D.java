package fbhackercup.s2016.round2.d;

import java.io.*;
import java.util.ArrayList;

class D {
    private static void main() throws IOException {
        int n = Parser.nextInt();
        int k = Parser.nextInt();
        long p = Parser.nextLong();
        long[][] c = new long[n][k];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                c[i][j] = Parser.nextInt();
            }
        }
        ArrayList<ArrayList<Integer>> g = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            g.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < n - 1; i++) {
            int x = Parser.nextInt() - 1;
            int y = Parser.nextInt() - 1;
            g.get(x).add(y);
            g.get(y).add(x);
        }

    }

    // Prewritten code


    static PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

    public static void main(String[] args) throws IOException {
        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            out.print("Case #" + (tt + 1) + ": ");
            main();
            out.println();
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
