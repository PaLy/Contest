from itertools import permutations
from multiprocessing.pool import Pool


def check(pick, mat, learn, por):
    n = len(mat)
    for i in range(n):
        wn = por[i]
        if not (mat[wn][pick[i]] == 1 or ((learn >> (wn * n + pick[i])) & 1) == 1):
            return False
    return True


def learned(w, n, learn, mat):
    res = []
    for i in range(n):
        if (learn >> (w * n + i)) & 1 == 1 or mat[w][i] == 1:
            res.append(i)
    return res


def solve(args):
    n, mat = args

    res = []
    for learn in range(1 << n * n):
        ok = True
        for por in permutations(range(n)):
            if not ok:
                break
            am1 = set(learned(por[0], n, learn, mat))
            if len(am1) == 0:
                ok = False
            for p1 in am1:
                if not ok:
                    break
                if n == 1:
                    if not check((p1,), mat, learn, por):
                        ok = False
                else:
                    am2 = set(learned(por[1], n, learn, mat))
                    am2.discard(p1)
                    if len(am2) == 0:
                        ok = False
                    for p2 in am2:
                        if not ok:
                            break
                        if n == 2:
                            if not check((p1, p2), mat, learn, por):
                                ok = False
                        else:
                            am3 = set(learned(por[2], n, learn, mat))
                            am3.discard(p1)
                            am3.discard(p2)
                            if len(am3) == 0:
                                ok = False
                            for p3 in am3:
                                if not ok:
                                    break
                                if (n == 3):
                                    if not check((p1, p2, p3), mat, learn, por):
                                        ok = False
                                else:
                                    am4 = set(learned(por[3], n, learn, mat))
                                    am4.discard(p1)
                                    am4.discard(p2)
                                    am4.discard(p3)
                                    if len(am4) > 0:
                                        p4 = next(iter(am4))
                                        if not check((p1, p2, p3, p4), mat, learn, por):
                                            ok = False
                                    else:
                                        ok = False
        if ok:
            res.append(learn)
    r = 1 << n
    for x in res:
        c = 0
        for i in range(n * n):
            if (x >> i) & 1 == 1:
                c += 1
        r = min(r, c)
    return r


t = int(input())
nfs = []
for tt in range(1, t + 1):
    n = int(input())
    mat = [[int(x) for x in input()] for _ in range(n)]
    nfs.append((n, mat))

with Pool(8) as p:
    res = p.map(solve, nfs)
    for tt in range(1, t + 1):
        print("Case #" + str(tt) + ":", res[tt - 1])
