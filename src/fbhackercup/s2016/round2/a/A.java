package fbhackercup.s2016.round2.a;

import java.io.*;

class A {
    private static void main(PrintWriter out) throws IOException {
    }

    // Prewritten code

    public static void main(String[] args) throws IOException {
        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
        int t = Parser.nextInt();
        for (int tt = 0; tt < t; ++tt) {
            out.print("Case #" + (tt + 1) + ": ");
            main(out);
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
