package fbhackercup.s2015.round1.d;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

class D {
    static int N = 200000;
    static int W = 25;
    static int[][] dp = new int[W][N];

    public static void main(String[] args) throws IOException {
        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            int n = Parser.nextInt();
            System.out.println("Case #" + (tt + 1) + ": " + solve(n));
        }
    }

    static ArrayList<ArrayList<Integer>> children;

    static int maxWeight = Integer.MIN_VALUE;

    private static int solve(int n) throws IOException {
        maxWeight = Integer.MIN_VALUE;

        for (int i = 0; i < W; i++) {
            Arrays.fill(dp[i], -1);
        }

        children = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            children.add(new ArrayList<Integer>());
        }
        for (int i = 0; i < n; i++) {
            int x = Parser.nextInt();
            if (i > 0) {
                children.get(x - 1).add(i);
            }
        }

        int min = Integer.MAX_VALUE;
        for (int i = 1; i < W; i++) {
            int f = f(i, 0);
//            if (f < min) {
//                maxWeight = Math.max(maxWeight, i);
//            }
            min = Math.min(min, f);
        }
//        System.out.println(maxWeight);
        return min;
    }

    private static int f(int weight, int node) {
        if (dp[weight][node] != -1) {
            return dp[weight][node];
        } else {
            int res = weight;
            for (int child : children.get(node)) {
                int r = Integer.MAX_VALUE;
                for (int i = 1; i < W; i++) {
                    if (i != weight) {
                        int f = f(i, child);
//                        if (f < r) {
//                            maxWeight = Math.max(maxWeight, i);
//                        }
                        r = Math.min(r, f);
                    }
                }
                res += r;
            }
            dp[weight][node] = res;
            return res;
        }
    }

    // Prewritten code

    private static class Parser {
        private static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        private static String line;
        private static ArrayList<String> stringArray = new ArrayList<>();
        private static int arrayPosition = 0;

        private static Integer nextInt() throws IOException {
            if (arrayPosition == stringArray.size()) {
                if (readLine() == null) return null;
            }
            return Integer.parseInt(stringArray.get(arrayPosition++));
        }

        private static Long nextLong() throws IOException {
            if (arrayPosition == stringArray.size()) {
                if (readLine() == null) return null;
            }
            return Long.parseLong(stringArray.get(arrayPosition++));
        }

        private static String nextString() throws IOException {
            if (arrayPosition == stringArray.size()) {
                if (readLine() == null) return null;
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
                stringArray = new ArrayList<>();
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
