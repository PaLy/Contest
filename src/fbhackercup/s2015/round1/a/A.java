package fbhackercup.s2015.round1.a;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

class A {
    public static void main(String[] args) throws IOException {
        int[] p = new int[10000001];
        Arrays.fill(p, 0);
        for (int i = 2; i < 10000001; i++) {
            if (p[i] == 0) {
                for (int j = i; j < 10000001; j += i) {
                    p[j] += 1;
                }
            }
        }

        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            int res = 0;
            Integer a = Parser.nextInt();
            Integer b = Parser.nextInt();
            Integer k = Parser.nextInt();
            for (int i = a; i <= b; i++) {
                if (p[i] == k) {
                    res++;
                }
            }
            System.out.println("Case #" + (tt + 1) + ": " + res);
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
