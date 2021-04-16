from multiprocessing.pool import Pool


def solve(args):
    n, k, p = args
    res = 0.0
    for m in range(1 << n):
        c = 0
        pa = []
        for i in range(n):
            if (m >> i) & 1 == 1:
                c += 1
                pa.append(p[i])
        if c == k:
            r = 0.0
            for mm in range(1 << k):
                c2 = 0
                pp = 1.0
                for i in range(k):
                    if (mm >> i) & 1 == 1:
                        c2 += 1
                        pp *= pa[i]
                    else:
                        pp *= 1 - pa[i]
                if c2 == k / 2:
                    r += pp
            res = max(res, r)
    return res


t = int(input())
nfs = []
for tt in range(1, t + 1):
    n, k = map(int, input().split())
    p = list(map(float, input().split()))
    nfs.append((n, k, p))

with Pool(8) as p:
    res = p.map(solve, nfs)
    for tt in range(1, t + 1):
        print("Case #" + str(tt) + ":", res[tt - 1])
