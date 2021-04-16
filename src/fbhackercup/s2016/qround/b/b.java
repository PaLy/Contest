package s2016.qual.b;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class b {
    public static void main(String[] args) throws IOException {
        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            int m = Parser.nextInt();
            int n = Parser.nextInt();
            Field[][] mapa = new Field[m][n];
            for (int i = 0; i < m; i++) {
                char[] chars = Parser.nextString().toCharArray();
                for (int j = 0; j < n; j++) {
                    mapa[i][j] = new Field(chars[j]);
                }
            }
            System.out.println("Case #" + (tt + 1) + ": " + solve(m, n, mapa));
        }
    }

    private static String solve(int m, int n, Field[][] mapa) {
        char[] turret = new char[]{'^', '>', 'v', '<'};
        int[] dx = new int[]{-1, 0, 1, 0};
        int[] dy = new int[]{0, 1, 0, -1};
        int sx = 0;
        int sy = 0;
        int gx = 0;
        int gy = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mapa[i][j].c == 'S') {
                    mapa[i][j].c = '.';
                    sx = i;
                    sy = j;
                } else if (mapa[i][j].c == 'G') {
                    mapa[i][j].c = '.';
                    gx = i;
                    gy = j;
                }
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int dir = 0; dir < turret.length; dir++) {
                    if (mapa[i][j].c == turret[dir]) {
                        for (int k = 0; k < 4; k++) {
                            int d = dir + k;
                            d %= 4;
                            int nx = i + dx[d];
                            int ny = j + dy[d];
                            while (check(nx, ny, mapa)) {
                                mapa[nx][ny].setNP(k);
                                nx += dx[d];
                                ny += dy[d];
                            }
                        }
                    }
                }
            }
        }

        Queue<State> queue = new PriorityQueue<>();
        queue.add(new State(sx, sy, 0));
        HashSet<State> done = new HashSet<>();
        while (!queue.isEmpty()) {
            State state = queue.poll();
            int x = state.x;
            int y = state.y;
            int time = state.time;
            if (x == gx && y == gy) {
                return String.valueOf(time);
            }
            done.add(state);
            int ntime = time + 1;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (check(nx, ny, mapa)) {
                    if (mapa[nx][ny].isPassable(ntime)) {
                        State newState = new State(nx, ny, ntime);
                        if (!done.contains(newState) && !queue.contains(newState)) {
                            queue.add(newState);
                        }
                    }
                }
            }
        }
        return "impossible";
    }

    private static boolean check(int nx, int ny, Field[][] mapa) {
        return nx >= 0 && nx < mapa.length && ny >= 0 && ny < mapa[0].length && mapa[nx][ny].c == '.';
    }

    // Prewritten code

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

    private static class Field {
        private char c;
        private Set<Integer> notPassable = new HashSet<>();

        public Field(char c) {
            this.c = c;
        }

        public void setNP(int dir) {
            notPassable.add(dir);
        }

        public boolean isPassable(int t) {
            return !notPassable.contains(t % 4);
        }
    }

    private static class State implements Comparable<State> {
        private final int x;
        private final int y;
        private final int time;
        private final int mtime;

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;

            State state = (State) o;

            if (mtime != state.mtime) return false;
            if (x != state.x) return false;
            if (y != state.y) return false;

            return true;
        }

        @Override
        public int hashCode() {
            int result = x;
            result = 31 * result + y;
            result = 31 * result + mtime;
            return result;
        }

        public State(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
            this.mtime = time % 4;

        }

        @Override
        public int compareTo(State o) {
            return Integer.valueOf(time).compareTo(o.time);
        }
    }
}
