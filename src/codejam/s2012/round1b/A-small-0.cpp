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

		int n;
		cin >> n;
		vector<int> v(n);
		FOR(i,0,n) cin >> v[i];

		int sum=0;
		FOR(i,0,n) sum+=v[i];

		FOR(i,0,n) {
		    int s=sum;
		    int m=v[i];
            vector<int> vv;
            FOR(j,0,n) if (j!=i) vv.PB(v[j]);

            FOR(j,0,n-1) if (vv[j]<m) { s-= m-vv[j]; vv[j]=m;}
            if (m<vv[0]) { s-=vv[0]-m; m=vv[0];}

            if (s>0) {
                sort(vv.begin(),vv.end());
                while(s) {
                    FOR(j,0,n-1) {
                        if (vv[j]==m && (j+1==n-1 || vv[j+1]>m)) {
                            m++;
                            s--;
                        }
                        if (s==0) break;
                        s--;
                        vv[j]++;
                        if (s==0 || (j+1<n+1 && vv[j]<=vv[j+1])) break;
                    }
                }
/*
                int q=0;
                FOR(j,0,n-1) if (vv[j]==m-1) q++;
                if (q>1 && m>v[i]) m-=1;
                */
            }

            printf("%.7lf", (m-v[i])*100.0/sum);
            if (i<n-1) cout << " ";
/*
            cout << m << " ";
            FOR(j,0,n-1) cout << vv[j] << " ";
            cout << endl;
*/
		}

		cout << endl;
	}
    return 0;
}

