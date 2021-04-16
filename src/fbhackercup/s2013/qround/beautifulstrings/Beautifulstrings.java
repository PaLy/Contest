package fbhackercup.s2013.qround.beautifulstrings;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

class Beautifulstrings {	
	public static void main(String[] args) throws IOException {
		int t = Parser.nextInt();
		for (int tt = 0; tt < t; ++tt) {
			String s = Parser.nextLine();
			
			System.out.println("Case #" + (tt + 1) + ": " + count(s));
		}
	}

	private static int count(String s) {
		int[] vyskyty = new int[26];
		Arrays.fill(vyskyty, 0);

		for (int i = 0; i < s.length(); ++i) {
			int id = Character.toLowerCase(s.charAt(i)) - 'a';
			if (id >= 26 || id < 0) continue;
			vyskyty[id]++;
		}

		Arrays.sort(vyskyty);
		int res = 0;
		for (int i = 0; i < 26; i++) {
			res += (i + 1) * vyskyty[i];
		}

		return res;
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
