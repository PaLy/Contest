package codejam.s2018.round1c;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    static int[][] d;
    static int[] w;

    public static void main() {
        try {
            Integer t = Parser.nextInt();
            for (int i = 0; i < t; i++) {
                solve(i);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void solve(int t) throws IOException {
        Integer n = Parser.nextInt();
        d = new int[n+1][7 * 1000 + 1];
        for (int i = 0; i < n+1; i++) {
            Arrays.fill(d[i], -1);
        }
        w = new int[n];
        for (int i = 0; i < n; i++) {
            w[i] = Parser.nextInt();
        }
        int sol = sol(n, 7 * 1000);
        System.out.println("Case #" + (t+1) + ": " + sol);
    }

    private static int sol(int e, int mw) {
        if (e == 1) {
            if (w[0] <= mw) {
                return 1;
            } else {
                return 0;
            }
        }
        if (d[e][mw] != -1) {
            return d[e][mw];
        } else {
            int res = 0;
            for (int i = 1; i < e; i++) {
                int mww = Math.min(6 * w[i], mw - w[i]);
                if (mww >= 0) {
                    res = Math.max(res, 1 + sol(i, mww));
                }
                res = Math.max(res, sol(i, mw));
            }
            d[e][mw] = res;
            return res;
        }
    }

    public static void main(String[] args) {
        main();
    }

    private static class Parser {
        private static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        private static String line;
        private static ArrayList<String> stringArray = new ArrayList<String>();
        private static int arrayPosition = 0;

        private static Integer nextInt() throws IOException {
            if (arrayPosition == stringArray.size()) {
                if (readLine() == null)
                    return null;
            }
            return Integer.parseInt(stringArray.get(arrayPosition++));
        }

        private static Long nextLong() throws IOException {
            if (arrayPosition == stringArray.size()) {
                if (readLine() == null)
                    return null;
            }
            return Long.parseLong(stringArray.get(arrayPosition++));
        }

        private static String nextString() throws IOException {
            if (arrayPosition == stringArray.size()) {
                if (readLine() == null)
                    return null;
            }
            return stringArray.get(arrayPosition++);
        }

        private static String nextLine() throws IOException {
            arrayPosition = stringArray.size();
            return in.readLine();
        }

        private static String readLine() throws IOException {
            line = in.readLine();
            if (line == null) {
                return null;
            } else {
                stringArray = new ArrayList<String>();
                arrayPosition = 0;

                int p, lastP = 0;
                while (true) {
                    p = line.indexOf(" ", lastP);
                    if (p == lastP) {
                        lastP++;
                    } else if (p != -1) {
                        stringArray.add(line.substring(lastP, p));
                        lastP = p + 1;
                    } else {
                        if (lastP < line.length()) {
                            stringArray.add(line.substring(lastP));
                        }
                        break;
                    }
                }
                return line;
            }
        }
    }
}
