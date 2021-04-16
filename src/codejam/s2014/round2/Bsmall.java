package codejam.s2014.round2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;

class Bsmall0 {
    public static void main(String[] args) throws IOException {
        int t = Parser.nextInt();
        for (int tt = 1; tt <= t; tt++) {
            System.out.println("Case #" + tt + ": " + solve());
        }
    }

    private static String solve() throws IOException {
        int n = Parser.nextInt();
        String cars[] = new String[n];
        for (int i = 0; i < n; i++) {
            cars[i] = Parser.nextString();
        }
        return String.valueOf(perm(0, cars, new ArrayList<Integer>()));
    }

    private static int perm(int i, String[] cars, ArrayList<Integer> pi) {
        if (i == cars.length) {
            StringBuilder s = new StringBuilder();
            for (int j = 0; j < pi.size(); j++) {
                s.append(cars[pi.get(j)]);
            }
            if (valid(s.toString())) {
                return 1;
            } else {
                return 0;
            }
        } else {
            int res = 0;
            for (int j = 0; j < cars.length; j++) {
                if (!pi.contains(j)) {
                    pi.add(j);
                    res += perm(i + 1, cars, pi);
                    pi.remove(pi.size() - 1);
                    res %= 1000000007;
                }
            }
            return res;
        }
    }

    private static boolean valid(String s) {
        HashMap<Character, Integer> lastVisited = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            Integer lv = lastVisited.get(c);
            if (lv != null && lv < i - 1) {
                return false;
            }
            lastVisited.put(c, i);
        }
        return true;
    }

    private static class Parser {
        private static final BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        private static String line;
        private static ArrayList<String> stringArray = new ArrayList<String>();
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
