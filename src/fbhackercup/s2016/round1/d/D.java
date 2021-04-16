package s2016.round1.d;

import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class D {
    private static void main() throws IOException {
        int n = Parser.nextInt();
        int k = Parser.nextInt();
        Node root = new Node();
        for (int i = 0; i < n; i++) {
            String w = Parser.nextString();
            Node curNode = root;
            for (int j = 0; j < w.length(); j++) {
                char c = w.charAt(j);
                Node nextNode = curNode.children.get(c);
                if (nextNode == null) {
                    nextNode = new Node();
                    curNode.children.put(c, nextNode);
                }
                curNode = nextNode;
            }
            curNode.word = true;
        }

        countRec(root);
        out.print(root.minPath[k]);
    }

    private static void countRec(Node root) {
        for (Node node : root.children.values()) {
            countRec(node);
        }
        for (Node child : root.children.values()) {
            int[] mp = new int[Node.K + 1];
            Arrays.fill(mp, Node.INF);
            for (int ri = 0; ri < Node.K + 1; ri++) {
                for (int i = 0; i < Node.K + 1; i++) {
                    if (child.minPath[i] != Node.INF && root.minPath[ri] != Node.INF) {
                        mp[i + ri] = Math.min(mp[i + ri], child.minPath[i] + 2 + root.minPath[ri]);
                    }
                }
            }
            for (int i = 0; i < Node.K + 1; i++) {
                root.minPath[i] = Math.min(root.minPath[i], mp[i]);
            }
        }
        if (root.word) {
            for (int i = Node.K - 1; i >= 0; i--) {
                if (root.minPath[i] != Node.INF) {
                    root.minPath[i + 1] = Math.min(root.minPath[i + 1], root.minPath[i] + 1);
                }
            }
        }
    }

    static class Node {
        private final Map<Character, Node> children = new HashMap<>();
        private final int[] minPath = new int[K + 1];
        private boolean word = false;
        public static int K = 300;
        public static int INF = Integer.MAX_VALUE / 2 - 5;

        public Node() {
            for (int i = 0; i < Node.K + 1; i++) {
                minPath[i] = INF;
            }
            minPath[0] = 0;
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
