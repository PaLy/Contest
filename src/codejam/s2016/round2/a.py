from itertools import permutations
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
    ss = p * 'P' + r * 'R' + s * 'S'
    done = set()
    for comb in permutations(ss, 1 << n):
        if comb in done:
            continue
        done.add(comb)
        c1 = comb
        ok = True
        for i in range(n):
            c2 = ()
            for j in range(len(c1) // 2):
                if c1[2 * j] == c1[2 * j + 1]:
                    ok = False
                    break
                cc = (winner(c1[2 * j], c1[2 * j + 1]),)
                c2 = c2 + cc
            if not ok:
                break
            c1 = c2
        if ok:
            return ''.join(x for x in comb)
    return "IMPOSSIBLE"


t = int(input())
nfs = []
for tt in range(1, t + 1):
    n, r, p, s = map(int, input().split())
    nfs.append((n, r, p, s))

with Pool(8) as p:
    res = p.map(solve, nfs)
    for tt in range(1, t + 1):
        print("Case #" + str(tt) + ":", res[tt - 1])
