#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>
#include <climits>

#include <cstdlib>
#include <algorithm>
#include <cmath>

#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <ctime>

using namespace std;

#define FOR(i,n1,n2) for(int i=n1;i<n2;i++)
#define FORD(i,n1,n2) for(int i=n1;i>=n2;i--)
#define FORE(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define PB push_back
#define MP make_pair
#define SZ(i) i.size()
#define FIR first
#define SEC second

int main() {
    int t;
    cin >> t;
    FOR(tt,0,t) {
        int n,m;
        cin >> n >> m;

        vector<int> f(n),t(n);
        FOR(i,0,m) {
            int x;
            cin >> x;
            f[i]=x-1;
        }
        FOR(i,0,m) {
            int x;
            cin >> x;
            t[i]=x-1;
        }

        map<int, vector<int> > edge;
        FOR(i,0,m) edge[f[i]].PB(t[i]);
        FOR(i,0,n) {
            edge[i].PB((i+1)%n);
            edge[(i+1)%n].PB(i);
        }


        set<set<int> > ss;

        FOR(i,0,n) {
            queue<int> Q;
            Q.push(i);
            vector<int> from(n),was(n,0);
            set<int> s;
            int kam=i+1;
            s.insert(i+1);
            while(kam!=i) {
                int max=-1;
                FOR(j,0,SZ(edge[kam])) {
                    if (edge[kam][j]-i-1>max) {
                        max=edge[kam][j]-i-1;
                    }
                }
                kam=max+i+1;
                s.insert(kam);
            }
            ss.insert(s);
        }

        FORE(it,ss) {
            FORE(it2,*it) cout << *it2 << " ";
            cout << endl;
        }

        int res=0;

        printf("Case #%d: %d\n", tt+1, res);
    }
    return 0;
}
