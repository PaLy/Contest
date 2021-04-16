package fbhackercup.s2015.round1.b;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class B {
    public static void main(String[] args) throws IOException {
        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            int n = Parser.nextInt();
            System.out.println("Case #" + (tt + 1) + ": " + solve(n));
        }
    }

    static class Node {
        Node[] childs = new Node[26];
    }

    private static long solve(int n) throws IOException {
        Node root = new Node();
        long res = 0;
        for (int i = 0; i < n; i++) {
            Node cur = root;
            String s = Parser.nextLine();
            boolean ok = false;
            for (int j = 0; j < s.length(); j++) {
                int c = s.charAt(j) - 'a';
                if (cur.childs[c] == null) {
                    if (!ok) {
                        res += j + 1;
                        ok = true;
                    }
                    cur.childs[c] = new Node();
                }
                cur = cur.childs[c];
            }
            if (!ok) {
                res += s.length();
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
