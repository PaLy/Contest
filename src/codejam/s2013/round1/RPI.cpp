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

double count_wp(string vs) {
    int win=0,loss=0;
    FOR(i,0,SZ(vs)) if (vs[i]=='1') win++; else if (vs[i]=='0') loss++;
    return win/(double)(win+loss);
}

int main() {
    int t;
    cin >> t;
    FOR(tt,0,t) {
        int n;
        cin >> n;
        vector<string> vs(n);
        FOR(i,0,n) cin >> vs[i];

        printf("Case #%d:\n", tt+1);

        vector<double> wp(n),owp(n,0),games(n,0);

        FOR(i,0,n) wp[i]=count_wp(vs[i]);

        FOR(nn,0,n)
            FOR(i,0,SZ(vs[nn])) if (vs[nn][i]!='.') games[nn]++;

        FOR(nn,0,n) {
            FOR(i,0,n) if (vs[nn][i]!='.') {
                string s=vs[i];
                s[nn]='.';
                owp[nn]+=count_wp(s)/(double)games[nn];
            }
        }


        FOR(nn,0,n) {
            double res=0;
            res+=0.25*wp[nn]+0.5*owp[nn];
            FOR(i,0,n) {
                if (vs[nn][i]!='.') res+=owp[i]/(double)games[nn]/4.0;
            }
            printf("%.12lf\n", res);
        }
    }
    return 0;
}
