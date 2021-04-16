d = dict()


def sol(e, mw, w):
    if e == 1:
        if mw == -1:
            return 1
        else:
            if w[0] <= mw:
                return 1
            else:
                return -1
    if (e, mw) in d:
        return d[(e, mw)]

    res = 0
    for i in reversed(range(1, e)):
        mww = 6 * w[i]
        if mw != -1:
            mww = min(mww, mw - w[i])
        if mww < 0:
            continue
        r = sol(i, mww, w)
        if r != -1:
            res = max(res, 1 + r)
        r = sol(i, mw, w)
        if r != -1:
            res = max(res, r)

    d[(e, mw)] = res
    return res


def solve():
    n = int(input())
    w = list(map(int, input().split()))

    return sol(n, -1, w)


t = int(input())
for tt in range(1, t + 1):
    d.clear()
    print("Case #" + str(tt) + ": " + str(solve()))
    print(len(d))
