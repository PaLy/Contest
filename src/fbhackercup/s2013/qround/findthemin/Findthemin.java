package fbhackercup.s2013.qround.findthemin;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;

class Findthemin {
	public static void main(String[] args) throws IOException {
		int t = Parser.nextInt();
		for (int tt = 0; tt < t; ++tt) {
			long n = Parser.nextLong();
			long k = Parser.nextLong();
			long a = Parser.nextLong();
			long b = Parser.nextLong();
			long c = Parser.nextLong();
			long r = Parser.nextLong();
			System.out.println("Case #" + (tt + 1) + ": " + solve(n, k, a, b, c, r));
		}
	}

	private static long solve(long n, long k, long a, long b, long c, long r) {
		HashMap<Long, Integer> used = new HashMap<Long, Integer>();

		long[] m = new long[(int) k];
		for (int i = 0; i < k; i++) {
			if (i > 0) {
				m[i] = (b * m[i - 1] + c) % r;
			} else {
				m[i] = a;
			}
			used.put(m[i], i);
		}

		long[] m2 = new long[(int) (k + 1)];

		long min = 0;
		while (used.containsKey(min)) min++;
		m2[0] = min;

		for (int i = 1; i < k + 1; i++) {
			if (used.get(m[i - 1]) == i - 1) {
				if (m[i - 1] < min) {
					m2[i] = m[i - 1];
					continue;
				} else {
					used.remove(m[i - 1]);
				}
			}

			min++;
			while (used.containsKey(min)) min++;
			m2[i] = min;
		}

		return m2[((int) ((n - k - 1) % (k + 1)))];
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
					} else {
						if (p != -1) {
							stringArray.add(line.substring(lastP, p));
						} else {
							stringArray.add(line.substring(lastP));
							break;
						}
						lastP = p + 1;
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
