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
        double res = 0.0;

        double x,s,r,ti,n;
        cin >> x >> s >> r >> ti >> n;

        vector<int> zac,kon,w;
        zac.PB(0);
        FOR(i,0,n) {
            int xx,yy,zz;
            cin >> xx >> yy >> zz;

            kon.PB(xx);
            w.PB(0);

            zac.PB(xx);
            kon.PB(yy);
            w.PB(zz);

            zac.PB(yy);
        }
        kon.PB(x);
        w.PB(0);



        FOR(i,0,SZ(zac)) {
            if (zac[i]==kon[i]) continue;
            double d = kon[i]-zac[i];
            if (w[i]==0) {
                double cesta=r*ti;
                if (cesta>=d) {
                    double time=d/r;
                    ti-=time;
                    res+=time;
                } else {
                    if (ti>0) {
                        double time=cesta/r;
                        ti=0;
                        res+=time;
                        d-=cesta;
                    }

                    double time = d/s;
                    res += time;
                }
            }
        }


        vector<pair<int,int> > v;
        FOR(i,0,SZ(zac)) if (w[i]) v.PB(MP(w[i],i));
        sort(v.begin(),v.end());
        //reverse(v.begin(),v.end());

        FOR(ii,0,SZ(v)) {
            int i=v[ii].second;
            if (zac[i]==kon[i]) continue;
            double d = kon[i]-zac[i];
            if (w[i]!=0) {
                double cesta=(r+w[i])*ti;
                if (cesta>=d) {
                    double time=d/(r+w[i]);
                    ti-=time;
                    res+=time;
                } else {
                    if (ti>0) {
                        double time=cesta/(r+w[i]);
                        ti=0;
                        res+=time;
                        d-=cesta;
                    }

                    double time = d/(s+w[i]);
                    res += time;
                }
            }
        }



        printf("Case #%d: %0.10lf\n", tt, res);
    }
    return 0;
}
