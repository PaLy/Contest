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

int main() {
    int t;
    cin >> t;
    FOR(tt,1,t+1) {
        int r,c,d;
        cin >> r >> c >> d;
        vector<string> v(r);
        FOR(i,0,r) cin >> v[i];

        int m=-1;

        FOR(zi,0,r) FOR(zj,0,c) FOR(ki,zi+2,r) {
            int kj=zj+(ki-zi);
            if (kj>=c) continue;
            double si=double(ki+zi)/2;
            double sj=double(kj+zj)/2;

            double a=0,b=0;
            FOR(i,zi,ki+1) FOR(j,zj,kj+1) {
                if ((i==zi && j==zj) || (i==ki && j==zj) || (i==zi && j==kj) || (i==ki && j==kj)) continue;
                a+=(v[i][j]-'0')*(i-si);
                b+=(v[i][j]-'0')*(j-sj);
            }
            if (a==0 && b==0) {
                if (kj-zj+1>m) m=kj-zj+1;
            }
        }

        cout << "Case #" << tt << ": ";
        if (m==-1) cout << "IMPOSSIBLE\n";
        else cout << m << endl;
    }
    return 0;
}
