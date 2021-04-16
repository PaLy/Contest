#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <climits>

#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <deque>
#include <forward_list>

#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <cmath>

#include <utility>

using namespace std;

#define FOR(i,n1,n2) for(int i = n1; i < n2; ++i)
#define FORD(i,n1,n2) for(int i = n1; i >= n2; --i)
#define FORE(e,c) for(auto& e : c)
#define SZ(i) (int) i.size()
#define PB push_back
#define MT make_tuple
#define g(c,i) get<i>(c)

int main() {
    int t;
	scanf("%d\n",&t);
	FOR(tt,1,t+1) {
		cout << "Case #" << tt << ": ";

		double d;
		int n,aa;
		cin >> d >> n >> aa;
		vector<double> x(n),t(n),a(aa);
        FOR(i,0,n) {
            cin >> t[i] >> x[i];
        }
        FOR(i,0,aa) cin >> a[i];




		cout << endl;
	}
    return 0;
}

