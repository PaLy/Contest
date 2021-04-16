from collections import Counter


def solveEasy():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    c = Counter()
    for x in a:
        c[x] += 1

    for k, v in c.items():
        if v >= d:
            return 0

    if d == 2:
        return 1
    else:
        for k, v in c.items():
            if v == 2:
                for x in a:
                    if x > k:
                        return 1
        for x in a:
            for y in a:
                if y == 2 * x:
                    return 1
        return 2


def solve():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    for i in range(n):
        for j in range(1, 51):
            a[i] = a[i] * j

    s = [{} for _ in range(n)]

    sizes = set()

    for i in range(n):
        for c in range(d):
            sizes.add(a[i] // (c + 1))
            s[i][a[i] // (c + 1)] = c

    res = d - 1

    for size in sizes:
        ok = []
        for i in range(n):
            if size in s[i]:
                ok.append((s[i][size], i))
        ok.sort()
        total = 0
        totalc = 0
        for i in range(len(ok)):
            c, _ = ok[i]
            total += c + 1
            totalc += c
            if total >= d:
                res = min(res, totalc)

                total -= c + 1
                totalc -= c
                need = d - total
                oki = set()
                for xxx in ok:
                    _, ii = xxx
                    oki.add(ii)
                for j in range(n):
                    if j not in oki and a[j] >= size:
                        tc = a[j] // size
                        if tc >= need:
                            res = min(res, totalc + need)
                        else:
                            need -= tc
                break

    return res


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve()))
