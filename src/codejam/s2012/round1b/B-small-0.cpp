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

int dx[]={0,0,1,-1};
int dy[]={1,-1,0,0};

int main() {
    int t;
	scanf("%d\n",&t);
	FOR(tt,1,t+1) {
		cout << "Case #" << tt << ": ";

		int h,n,m;
		cin >> h >> n >> m;
		vector<vector<int>> c(n),f(n);
		FOR(i,0,n) FOR(j,0,m) {
		    int x;
		    cin >> x;
		    c[i].PB(x);
		}
		FOR(i,0,n) FOR(j,0,m) {
		    int x;
		    cin >> x;
		    f[i].PB(x);
		}

		double d[n][m];

		FOR(i,0,n) FOR(j,0,m) d[i][j]=-1.0;
		d[0][0]=0;

		priority_queue<tuple<int,double>> q;
		q.push(MT(0,0));

		while(!q.empty()) {
            int ni=g(q.top(),0)/1000;
            int mi=g(q.top(),0)%1000;
            double t=g(q.top(),1);
            q.pop();
            if (d[ni][mi]<t) continue;//?
            FOR(i,0,4) {
                int nii=ni+dx[i];
                int mii=mi+dy[i];
                if (mii<0 || nii<0 || mii==m || nii==n
                    || c[nii][mii]-50<f[ni][mi] || c[nii][mii]-50<f[nii][mii]
                    || c[ni][mi]-50<f[nii][mii]) continue;
                double tt=(h+50-c[nii][mii]);
                tt=max(tt,t);
                double hh=h-tt;
                if (hh!=h) {
                    if (hh-20>=f[ni][mi]) tt+=10; else tt+=100;
                }

                if (d[nii][mii]==-1 || d[nii][mii]>tt) {
                    d[nii][mii]=tt;
                    q.push(MT(nii*1000+mii,tt));
                }
            }
		}

        printf("%.7lf\n", d[n-1][m-1]*0.1);
	}
    return 0;
}

