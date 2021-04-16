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

bool ok(vector<double> v, int d) {
    FOR(i,0,SZ(v)-1) if (abs(v[i]-v[i+1])<(double)d) return 0;
    return 1;
}

int main() {
    int t;
    cin >> t;
    FOR(tt,0,t) {
        double time=0;

        int c,d;
        cin >> c >> d;
        vector<double> v;
        FOR(i,0,c) {
            int p, ve;
            cin >> p >> ve;
            FOR(j,0,ve) v.PB(p);
        }

        while(!ok(v,d)) {
            time+=0.5;
            v[0]-=0.5;
            FOR(i,1,SZ(v))
                if (v[i]-v[i-1]>d) v[i]-=0.5;
                else if (v[i]-v[i-1]==d) continue;
                else v[i]+=0.5;
        }

        printf("Case #%d: %lf\n", tt+1, time);
    }
    return 0;
}
