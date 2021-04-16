from collections import Counter
from multiprocessing.pool import Pool


def winner(a, b):
    aa = min(a, b)
    bb = max(a, b)
    if aa == 'P' and bb == 'R':
        return 'P'
    elif aa == 'P' and bb == 'S':
        return 'S'
    elif aa == 'R' and bb == 'S':
        return 'R'


def solve(args):
    n, r, p, s = args
    ww = ['P', 'S', 'R']
    res = []
    for w in ww:
        t = (w,)
        for i in range(n):
            t2 = ()
            for j in range(len(t)):
                if t[j] == 'P':
                    t2 += ('P', 'R')
                elif t[j] == 'R':
                    t2 += ('R', 'S')
                else:
                    t2 += ('P', 'S')
            t = t2
        cc = Counter(t)
        if cc['P'] == p and cc['R'] == r and cc['S'] == s:
            res.append(''.join(x for x in t))

    if len(res) == 0:
        return "IMPOSSIBLE"
    else:
        pres = []
        for r in res:
            for k in range(n):
                q = []
                for i in range(len(r) // 2):
                    aa = min(r[2 * i], r[2 * i + 1])
                    bb = max(r[2 * i], r[2 * i + 1])
                    q.append(aa + bb)
                r = q
            pres.append(r)
        return ''.join(x for x in min(pres))


t = int(input())
nfs = []
for tt in range(1, t + 1):
    n, r, p, s = map(int, input().split())
    nfs.append((n, r, p, s))

with Pool(8) as p:
    res = p.map(solve, nfs)
    for tt in range(1, t + 1):
        print("Case #" + str(tt) + ":", res[tt - 1])
