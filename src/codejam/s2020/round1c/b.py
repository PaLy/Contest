from collections import Counter


def dd(x):
    res = 0
    last = 0
    while x > 0:
        last = x
        x //= 10
        res += 1
    return res, last


def solve():
    u = int(input())

    lt = {}
    allchrs = set()

    for _ in range(10000):
        qs, r = input().split()
        q = int(qs)

        for x in r:
            allchrs.add(x)

        ddq, first = dd(q)
        if r[0] not in lt:
            lt[r[0]] = 9
        if len(r) == ddq:
            lt[r[0]] = min(int(first), lt.get(r[0]))

    res = ['.'] * 10
    for k, v in lt.items():
        res[v] = k
        allchrs.remove(k)

    for x in allchrs:
        res[0] = x

    return ''.join(x for x in res)


def solve2():
    u = int(input())

    c = Counter()
    allchrs = set()

    for i in range(10000):
        qs, r = input().split()
        for x in r:
            allchrs.add(x)
        c[r[0]] += 1

    ll = [(v, k) for k, v in c.items()]
    ll.sort(reverse=True)

    res = ['.'] * 10
    for i in range(len(ll)):
        _, k = ll[i]
        res[i + 1] = k
        allchrs.remove(k)

    for x in allchrs:
        res[0] = x

    return ''.join(x for x in res)


t = int(input())
for tt in range(1, t + 1):
    print("Case #" + str(tt) + ": " + str(solve2()))
