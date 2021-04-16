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
		cout << "Case #" << tt << ":\n";

        int n;
        cin >> n;
        vector<int> v(n);
        FOR(i,0,n) cin >> v[i];

        FOR(m,0,1<<20) {
            int s1=0;
            int s2=0;
            FOR(k,0,20) if (m&(1<<k)) s1+=v[k]; else s2+=v[k];
            if (s1==s2) {
                vector<int> f1,f2;
                FOR(k,0,20) if (m&(1<<k)) f1.PB(v[k]); else f2.PB(v[k]);
                FOR(i,0,SZ(f1)-1) cout << f1[i] << " ";
                cout << f1[SZ(f1)-1] << endl;
                FOR(i,0,SZ(f2)-1) cout << f2[i] << " ";
                cout << f2[SZ(f2)-1] << endl;
                goto next;
            }
        }

        cout << "Impossible";

		cout << endl;
		next:;
	}
    return 0;
}

