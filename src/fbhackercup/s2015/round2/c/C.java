package fbhackercup.s2015.round2.c;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

class C {
    static int k;

    public static void main(String[] args) throws IOException {
        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            int n = Parser.nextInt();
            k = Parser.nextInt();
            System.out.println("Case #" + (tt + 1) + ": " + solve(n));
        }
    }

    static class Node {
        HashMap<Character, Node> childs = new HashMap<>();
        int depth;
        boolean hit;
        long[] dp = new long[k + 1];

        public Node(int depth) {
            this.depth = depth;
            Arrays.fill(dp, -2);
        }
    }

    private static long solve(int n) throws IOException {
        Node root = new Node(0);
        for (int i = 0; i < n; i++) {
            Node cur = root;
            String s = Parser.nextLine();
            for (int j = 0; j < s.length(); j++) {
                char c = s.charAt(j);
                Node child = cur.childs.get(c);
                if (child == null) {
                    cur.childs.put(c, new Node(cur.depth + 1));
                }
                cur = cur.childs.get(c);
            }
            cur.hit = true;
        }
        
        return countDP(root, k);
    }

    private static long countDP(Node node, int k) {
        if (node.dp[k] != -2) {
            return node.dp[k];
        }
        if (k == 0) {
            return 0;
        } else if (node.childs.size() == 0) {
            if (k == 1) {
                return 1;
            } else {
                return -1;
            }
        } else {
            long[] kk = new long[k + 1];
            Arrays.fill(kk, -1);
            kk[0] = 0;
            for (Node child : node.childs.values()) {
                long[] kk2 = new long[k + 1];
                for (int i = 0; i < k + 1; i++) {
                    kk2[i] = countDP(child, i);
                }
                kk = merge(node.depth, kk, kk2);
            }
            if (node.hit) {
                for (int i = k; i >= 2; i--) {
                    if (kk[i - 1] != -1 || kk[i] > kk[i - 1] + node.depth) {
                        kk[i] = kk[i - 1] + node.depth;
                    }
                }
                kk[1] = node.depth;
            }
            node.dp[k] = kk[k];
            return kk[k];
        }
    }

    private static long[] merge(int depth, long[] kk, long[] kk2) {
        int n = kk.length;
        long[] res = new long[n];
        Arrays.fill(res, -1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                int si = i - j;
                if (kk[si] != -1 && kk2[j] != -1) {
                    long val1 = kk[si];
                    long val2 = kk2[j];
                    if (si == 1) {
                        val1 = depth + 1;
                    }
                    if (j == 1) {
                        val2 = depth + 1;
                    }
                    if (res[i] == -1 || res[i] > val1 + val2) {
                        res[i] = val1 + val2;
                    }
                }
            }
        }
        return res;
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
