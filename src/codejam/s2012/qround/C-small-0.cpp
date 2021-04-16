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

#define MAX 2000047
vector<set<int>> v(MAX);

int main() {
    int t;
    cin >> t;
    int l=1;
    int k=10;
    int p=0;
    FOR(i,0,MAX) {
        int x=i;
        FOR(ii,0,l-1) {
            int m=x%10;
            x/=10;
            if (m!=0) {
                x+=m*pow(10,l-1);
                if (x>i) v[i].insert(x);
            }
        }

        p++;
        if (p==k) {
            k*=10;
            l+=1;
        }
    }

    FOR(tt,1,t+1) {
        cout << "Case #" << tt << ": ";

        int a,b;
        cin >> a >> b;
        int res=0;
        FOR(i,a,b+1) {
            FORE(e,v[i])
                if (e>=a && e<=b) {
                res++;
            }
        }

        cout << res << endl;
    }
    return 0;
}

