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

		int n,D;
		cin >> n;
		vector<int> d(n),l(n);
		FOR(i,0,n) cin >> d[i] >> l[i];
		cin >> D;

		int pos=0,c=0;
		int best=-1;
		int maxbest=0;

        if (D-d[0]<=l[0]) {
            cout << "YES";
            goto next;
        }
		FOR(i,1,n) {
            if (i < n && d[i]-d[c]<=d[c]-pos) {
                int mb=d[i]+min(d[i]-d[c],l[i]);
                if (mb>=D) {
                    //cout << endl << c << " " << i << " " << mb << endl;
                    cout << "YES";
                    goto next;
                }
                if (best=-1 || mb>maxbest) {
                    best=i;
                    maxbest=mb;
                }
            } else {
                if (best==-1) {
                    cout << "NO";
                    goto next;
                } else {
                    pos=d[best]-min(d[best]-d[c],l[best]);
                    c=best;
                    i=c;
                    best=-1;
                }
            }
		}

		cout << "NO";

		next:;
		cout << endl;
	}
    return 0;
}

