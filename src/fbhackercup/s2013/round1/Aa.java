package fbhackercup.s2013.round1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

class Aa {
	private static final long MOD = 1000000007;

	public static void main(String[] args) throws IOException {
		gen(10047, 10047);
		int t = Parser.nextInt();
		for (int tt = 0; tt < t; ++tt) {
			long n = Parser.nextLong();
			long k = Parser.nextLong();
			long[] pole = new long[(int) n];
			for (int i = 0; i < n; i++) {
				pole[i] = Parser.nextLong();
			}
			System.out.println("Case #" + (tt + 1) + ": " + solve(n, k, pole));
		}
	}

	private static long solve(long n, long k, long[] pole) {
		Arrays.sort(pole);
		long sum = 0;
		for (int i = (int) k - 1; i < n; i++) {
			long moznosti = bin[i][((int) (k - 1))];
			sum += moznosti * pole[i];
			sum %= MOD;
		}
		return sum;
	}

	static long[][] bin;

	private static void gen(int n, int k) {
		bin = new long[n + 1][k + 1];
		for (int i = 0; i < n + 1; i++) {
			for (int j = 0; j < k + 1; j++) {
				bin[i][j] = 0;
			}
		}
		bin[0][0] = 1;
		bin[1][0] = 1;
		bin[1][1] = 1;
		for (int i = 2; i < n + 1; i++) {
			bin[i][0] = 1;
			for (int j = 1; j < i + 1; j++) {
				bin[i][j] = bin[i - 1][j - 1] + bin[i - 1][j];
				bin[i][j] %= MOD;
			}
		}
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

	private static class Tuple implements Comparable<Tuple> {
		int[] x;

		private Tuple(int... xs) {
			x = new int[xs.length];
			System.arraycopy(xs, 0, x, 0, xs.length);
		}

		@Override
		public int compareTo(Tuple o) {
			for (int i = 0; i < x.length && i < o.x.length; ++i) {
				if (x[i] < o.x[i]) {
					return -1;
				} else if (x[i] > o.x[i]) {
					return 1;
				}
			}
			return 0;
		}

		@Override
		public boolean equals(Object obj) {
			if (obj instanceof Tuple) {
				for (int i = 0; i < x.length && i < ((Tuple) obj).x.length; ++i) {
					if (x[i] != ((Tuple) obj).x[i]) {
						return false;
					}
				}
				return true;
			}
			return false;
		}
	}

	static boolean nextPermutation(int[] p) {
		for (int i = p.length - 2; i >= 0; --i) {
			if (p[i] < p[i + 1]) for (int j = p.length - 1; ; --j) {
				if (p[j] > p[i]) {
					int t = p[i];
					p[i] = p[j];
					p[j] = t;
					for (++i, j = p.length - 1; i < j; ++i, --j) {
						t = p[i];
						p[i] = p[j];
						p[j] = t;
					}
					return true;
				}
			}
		}
		return false;
	}
}
