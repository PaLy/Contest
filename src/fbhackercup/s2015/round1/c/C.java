package fbhackercup.s2015.round1.c;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

class C {
    static int[][] sfr = new int[2001][2001];
    static int[][] sfu = new int[2001][2001];

    public static void main(String[] args) throws IOException {
        for (int i = 0; i < 2001; i++) {
            Arrays.fill(sfr[i], -1);
            Arrays.fill(sfu[i], -1);
        }
        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            String s = Parser.readLine();
            String[] split = s.split("-");
            int x = Integer.parseInt(split[0]);
            int y = Integer.parseInt(split[1]);
            System.out.println("Case #" + (tt + 1) + ": " + countSFR(x, y) + " " + countSFU(y - 1, y));
        }
    }

    private static int countSFU(int x, int y) {
        if (x <= 0 && y == 0) {
            return 1;
        } else if (sfu[x][y] != -1) {
            return sfu[x][y];
        } else {
            int res = 0;
            if (x > 0) {
                res += countSFU(x - 1, y);
            }
            if (x <= y - 1) {
                res += countSFU(x, y - 1);
            }
            sfu[x][y] = res % 1000000007;
            return sfu[x][y];
        }
    }

    private static int countSFR(int x, int y) {
        if (sfr[x][y] != -1) {
            return sfr[x][y];
        } else if (x == 1 && y == 0) {
            return 1;
        } else {
            int res = 0;
            if (y > 0) {
                res += countSFR(x, y - 1);
            }
            if (x - 1 > y) {
                res += countSFR(x - 1, y);
            }
            sfr[x][y] = res % 1000000007;
            return sfr[x][y];
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
