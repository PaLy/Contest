package fbhackercup.s2013.qround.balancedsmileys;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

class Balancedsmileys {
	public static void main(String[] args) throws IOException {
		int t = Parser.nextInt();
		for (int tt = 0; tt < t; ++tt) {
			String s = Parser.nextLine();

			System.out.println("Case #" + (tt + 1) + ": " + solve(s));
		}
	}

	private static String solve(String s) {
		int opened = 0;
		int smiley = 0;
		int frowny = 0;
		for (int i = 0; i < s.length(); ++i) {
			char c = s.charAt(i);
			if (c == '(') {
				if (i > 0 && s.charAt(i - 1) == ':') {
					frowny++;
				} else {
					smiley = Math.min(smiley, opened);
					opened++;
				}
			} else if (c == ')') {
				if (i > 0 && s.charAt(i - 1) == ':') {
					smiley++;
				} else if (opened > 0) {
					opened--;
				} else if (frowny > 0) {
					frowny--;
				} else {
					return "NO";
				}
			}
		}

		System.out.println(smiley);
		if (smiley >= opened) {
			return "YES";
		} else {
			return "NO";
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
