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
    cin >> t;
    FOR(tt,1,t+1) {
        cout << "Case #" << tt << ": ";

        int n,s,p;
        cin >> n >> s >> p;
        vector<int> v(n);
        FOR(i,0,n) cin >> v[i];

        int res=0,res2=0;
        FOR(i,0,n) {
            if (3*(p-1)<v[i]) res++;
            else if (v[i]==0 && p>0);
            else if (v[i]>=3*(p-1)-1) res2++;
        }
        res+=min(s,res2);

        cout << res << endl;
    }
    return 0;
}

